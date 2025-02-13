from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts.prompt import PromptTemplate

def format_docs(docs):
    if not docs:
        return "I don't know."
    return "\n\n".join(doc.page_content for doc in docs)


# 1. Load vectorstore from chromadb from step 1
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="demo.db",
    collection_name="demo_web"
)

query = "RAG คืออะไร"

# 2. Re-ranking the documents with Cohere
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

compressor = CohereRerank(model="rerank-english-v3.0")
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

# 3. Define the RAG pipeline with Re-ranking the documents
template = """You are an assistant for question-answering tasks. 
Use only the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.

Question: {question} 
Context: {context} 
Answer:
"""

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
prompt = PromptTemplate.from_template(template=template)

rag_chain = (
    {"context": compression_retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 4. Run the pipeline
result = rag_chain.invoke("RAG คืออะไร")
print("Result:", result)