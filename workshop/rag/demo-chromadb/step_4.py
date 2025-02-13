import os 
os.environ['USER_AGENT'] = 'demoagent'

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts.prompt import PromptTemplate


# Load vectorstore from chromadb from step 1
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="demo.db",
    collection_name="demo_web"
)

# 1. Define the retriever with k=1 (result = 1 document)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

# 2. Define the RAG pipeline.
# https://smith.langchain.com/hub/rlm/rag-prompt
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
result = rag_chain.invoke("RAG คืออะไร")
print("Result:", result)