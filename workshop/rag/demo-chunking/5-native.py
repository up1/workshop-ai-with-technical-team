from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Step 1: Load the document
loader = PyPDFLoader("./data/1810.04805v2.pdf")
documents = loader.load()
print(f"Pages= {len(documents)}")

# Step 2: Split the document into chunks with RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False
)

naive_chunks = text_splitter.split_documents(documents)
print(f"Chunks= {len(naive_chunks)}")
# Print the first 3 chunks
# for chunk in naive_chunks[0:3]:
#   print(chunk.page_content+ "\n\n")

# Step 3: Embedding the chunks with BAAI/bge-base-en-v1.5 from Huggingface
embed_model = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")

# Step 4: Store in vector database
db = FAISS.from_documents(naive_chunks, embed_model)
# db.save_local("native-chunk")

# Step 5: Query the vector database with the query and retrieve the top-k chunks
from langchain_core.prompts import ChatPromptTemplate

rag_template = """\
Use the following context to answer the user's query. If you cannot answer, please respond with 'I don't know'.

User's Query:
{question}

Context:
{context}
"""

rag_prompt = ChatPromptTemplate.from_template(rag_template)

# Step 7: Generate the final answer
MODEL_NAME = "llama3.2:1b"
client = ChatOllama(
    base_url = 'http://localhost:11434',
    api_key='ollama', # required, but unused
    model=MODEL_NAME,
)


naive_chunk_retriever = db.as_retriever(search_kwargs={"k" : 5})
naive_rag_chain = (
    {"context" : naive_chunk_retriever, "question" : RunnablePassthrough()}
    | rag_prompt
    | client
    | StrOutputParser()
)

response = naive_rag_chain.invoke("Describe the Feature-based Approach with BERT?")
print(response)


