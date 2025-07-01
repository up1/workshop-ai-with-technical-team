from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data.pdf")
pages = loader.load_and_split()

# Find and replan newline characters
for page in pages:
    if "\n" in page.page_content:
        page.page_content = page.page_content.replace("\n", " ")    

# Create embeddings and store the documents in a FAISS index
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(pages, embeddings)
db.save_local("faiss_index")
print("FAISS index saved to 'faiss_index'.")