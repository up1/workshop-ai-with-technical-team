from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# load data
documents = SimpleDirectoryReader(input_dir="./01-data/").load_data()

# build VectorStoreIndex that takes care of chunking documents
# and encoding chunks to embeddings for future retrieval
index = VectorStoreIndex.from_documents(documents=documents)

# The QueryEngine class is equipped with the generator
# and facilitates the retrieval and generation steps
query_engine = index.as_query_engine()

# Use your Default RAG
response = query_engine.query("สีเหลือง")
print(response)
