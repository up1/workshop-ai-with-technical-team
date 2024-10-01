from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

query = "How to calculate the median of an array and show example code"

embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
docs = db.similarity_search(query)

chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff")
print(chain.invoke({"input_documents": docs, "question": query}, return_only_outputs=True))