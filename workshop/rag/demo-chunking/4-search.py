from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

query = "How to calculate the median of an array and show example code"

# Load embeddings and the FAISS index
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("fifa_world_cup.faiss", embeddings, allow_dangerous_deserialization=True)
relevant_data = db.similarity_search(query)
print(len(relevant_data))
print(relevant_data[0])