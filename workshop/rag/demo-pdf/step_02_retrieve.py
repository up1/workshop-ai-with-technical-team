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

# Print the retrieved documents
print("Retrieved Documents:")
for doc in docs:
    print(doc.metadata.get("source", "no-name"), " page=" , doc.metadata.get("page", 0), ":", doc.page_content[:100])
