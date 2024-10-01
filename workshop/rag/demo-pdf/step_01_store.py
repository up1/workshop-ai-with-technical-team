from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("numpy-ref.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(pages, embeddings)
db.save_local("faiss_index")