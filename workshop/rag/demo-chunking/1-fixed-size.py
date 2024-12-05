from langchain_text_splitters import CharacterTextSplitter

# Load an example document
with open("./data/1.txt") as f:
    data = f.read()

# Split the document into fixed-size chunks
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

# Create the documents
metadatas = [{"document": 1}, {"document": 2}]
documents = text_splitter.create_documents(
    [data, data], metadatas=metadatas
)
print(documents[0])

