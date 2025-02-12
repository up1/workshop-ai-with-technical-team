from utils import setup_environment
from loader import load_and_process_documents, create_vectorstore
from rag import create_rag_chain

def main():
    setup_environment()
    
    # Load and process documents
    url = "https://en.wikipedia.org/wiki/Chroma_(vector_database)"
    splits = load_and_process_documents(url)
    
    # Create vector store
    vectorstore = create_vectorstore(splits)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    
    # Create and run RAG chain
    rag_chain = create_rag_chain(retriever)
    result = rag_chain.invoke("What is chroma?")
    print(result)
    
    # Cleanup
    vectorstore.delete_collection()

if __name__ == "__main__":
    main()
