from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

DB_DIR = "chroma_db"
COLLECTION_NAME = "semantic_caching"

def get_from_cache(query):
    # Load the vectorstore from disk
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory=DB_DIR,
        collection_name=COLLECTION_NAME
    )
    
    # Search for the query in the vectorstore
    results = vectorstore.similarity_search_with_relevance_scores(query=query, k=1)
    for result, score in results:
       print(f"Retrieved from cache: {result.page_content} with score: {score}")
       if score > 0.8:
          return result.metadata["response"]
    return None

    
def store_in_cache(query, response):
    # Load the vectorstore from disk
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory=DB_DIR,
        collection_name=COLLECTION_NAME
    )
    
    # Store the query and response in the vectorstore
    cached_document = Document(page_content=query, metadata={"response": response})
    vectorstore.add_documents([cached_document])
    print(f"Stored in cache: {query} -> {response}")