import os 
os.environ['USER_AGENT'] = 'demoagent'

import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# 1. Load, chunk and index the contents from wikipedia and save to Vector DB(ChromaDB)
loader = WebBaseLoader(
    web_paths=(
        "https://aws.amazon.com/th/what-is/retrieval-augmented-generation/",
    ),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(class_="eb-faq-content")
    ),
)
docs = loader.load()

# 2. Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# 3. Save vectorstore to disk
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OpenAIEmbeddings(),
    persist_directory="demo.db",
    collection_name="demo_web"
)

print("Vectorstore saved to disk")