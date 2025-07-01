from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.schema import HumanMessage, SystemMessage

question = "ประเภทของสมาชิกมีอะไรบ้าง"

# Load embeddings and the FAISS index
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Search for relevant documents
docs = db.similarity_search(question)
db2 = FAISS.from_documents(docs, embeddings)


# Initialize the new chain
prompt_template = ChatPromptTemplate.from_template("You are a helpful assistant, Answer any use questions based solely on the context below: {context}")
chain = create_stuff_documents_chain(llm=ChatOpenAI(temperature=0, model="gpt-4.1"), prompt=prompt_template)
rag_chain = create_retrieval_chain(db2.as_retriever(), chain)

# Invoke the chain with the required inputs
result = rag_chain.invoke({"input": question})


# Print the result
print(result)

print("======== Result ========")
print("Question:", question)
print(result["answer"])