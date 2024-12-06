from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Step 1: Load the document
loader = PyPDFLoader("./data/1810.04805v2.pdf")
documents = loader.load()
print(f"Pages= {len(documents)}")

# Step 2: Split the document into chunks with SemanticChunker
embed_model = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
semantic_chunker = SemanticChunker(embed_model, breakpoint_threshold_type="percentile")
semantic_chunks = semantic_chunker.create_documents([d.page_content for d in documents])
print(f"Chunks= {len(semantic_chunks)}")
print(semantic_chunks[0].page_content)

# Find the chunk with the title "Effect of Pre-training Tasks"
for semantic_chunk in semantic_chunks:
  if "Feature-based Approach with BERT" in semantic_chunk.page_content:
    print(len(semantic_chunk.page_content))
    print(semantic_chunk.page_content)
exit()

# Step 3: Store in vector database
db = FAISS.from_documents(semantic_chunks, embed_model)
# db.save_local("semantic-chunk")

# Step 4: Query the vector database with the query and retrieve the top-k chunks
from langchain_core.prompts import ChatPromptTemplate

rag_template = """\
Use the following context to answer the user's query. If you cannot answer, please respond with 'I don't know'.

User's Query:
{question}

Context:
{context}
"""

rag_prompt = ChatPromptTemplate.from_template(rag_template)

# Step 5: Generate the final answer
MODEL_NAME = "llama3.2:1b"
client = ChatOllama(
    base_url = 'http://localhost:11434',
    api_key='ollama', # required, but unused
    model=MODEL_NAME,
)

naive_chunk_retriever = db.as_retriever(search_kwargs={"k" : 1})
naive_rag_chain = (
    {"context" : naive_chunk_retriever, "question" : RunnablePassthrough()}
    | rag_prompt
    | client
    | StrOutputParser()
)

response = naive_rag_chain.invoke("What is the purpose of Ablation Studies?")
print(response)


