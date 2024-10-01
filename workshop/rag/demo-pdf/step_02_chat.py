from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

query = "How to calculate the median of an array and show example code"

# Load embeddings and the FAISS index
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
docs = db.similarity_search(query)
db2 = FAISS.from_documents(docs, embeddings)


# Initialize the new chain
prompt_template = ChatPromptTemplate.from_template("Please summarize the following documents: {context}")
chain = create_stuff_documents_chain(llm=OpenAI(temperature=0), prompt=prompt_template)
rag_chain = create_retrieval_chain(db2.as_retriever(), chain)

# Invoke the chain with the required inputs
result = rag_chain.invoke({"input": query})



# Print the result
print(result)
print(result["answer"])