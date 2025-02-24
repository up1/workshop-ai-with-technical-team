from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_pdfs(chunk_size=3000, chunk_overlap=100):
    # load the pdf documents
    loader=PyPDFDirectoryLoader("data")
    documents=loader.load()

    # split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                   chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents=documents)
    print(docs)
    return docs