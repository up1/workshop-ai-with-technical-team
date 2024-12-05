from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
import pickle

# Load an example document
with open("./data/1.txt") as f:
    data = f.read()

# Split the document into fixed-size chunks
text_splitter = CharacterTextSplitter(
    separator="\n\n",   #The character that should be used to split
    chunk_size=1000,    #The size of the chunks
    chunk_overlap=200,  #The overlap between the chunks
    length_function=len,
    is_separator_regex=False,
)

# Create chunks
chunks=text_splitter.create_documents([data])
print(f"The number of chunks created : {len(chunks)}")
print(f"The first chunk is : {chunks[0]}")

# Save the chunks to vector files
# embeddings = OpenAIEmbeddings()
# vectorstore = FAISS.from_documents(chunks, embeddings)
# vectorstore.save_local("vectorstore-db")
