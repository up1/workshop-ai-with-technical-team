from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter


def read_data_and_convert_to_vector(file_path):
    # Solution 1 :: Load and split the text data
    loader = TextLoader(file_path)
    content = loader.load_and_split()
    vectorstore = FAISS.from_documents(content, OpenAIEmbeddings())

    # Solution 2 :: Load and split data with CharacterTextSplitter
    # loader = TextLoader(file_path)
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # content = text_splitter.split_documents(loader.load())
    # vectorstore = FAISS.from_documents(content, OpenAIEmbeddings())

    # Solution 3 :: Load and split data with RecursiveCharacterTextSplitter
    # loader = TextLoader(file_path)
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # content = text_splitter.split_documents(loader.load())
    # vectorstore = FAISS.from_documents(content, OpenAIEmbeddings())

    return vectorstore

# function main
if __name__ == "__main__":
    file_path = "page_1_fixed.txt"
    vectorstore = read_data_and_convert_to_vector(file_path)
    vectorstore.save_local("data.faiss")
    print("Vector store saved to data.faiss")
