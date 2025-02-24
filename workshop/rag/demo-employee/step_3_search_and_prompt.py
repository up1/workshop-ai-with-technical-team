from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts.prompt import PromptTemplate

# Load vectorstore from chromadb from step 1
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="employee_db",  # updated persist directory
    collection_name="demo_employee"
)

# 1. Define the retriever with k=2 (result = 2 document)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 2. Define the RAG pipeline.
# https://smith.langchain.com/hub/rlm/rag-prompt
template = """You are an Human Resource System within a corporate company. 
Use only the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.

Question: {question} 
Context: {context} 
Answer:
"""

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
prompt = PromptTemplate.from_template(template=template)

# Format the docs to be used in the prompt
def format_docs(docs):
    print(docs)
    if not docs:
        return "I don't know."
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 3. Run the pipeline
result = rag_chain.invoke("Who is the CEO of the company?")
print("Result:", result)