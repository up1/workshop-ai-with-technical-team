from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import SQLiteVSS
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings


# Load the document using a LangChain text loader
loader = TextLoader("data.txt")
documents = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter (chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
texts = [doc.page_content for doc in docs]
print (texts)

# Use the sentence transformer package with the all-MiniLM-L6-v2 embedding model 
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  

# Load the text embeddings in SQLiteVSS in a table named state_union
db = SQLiteVSS.from_texts(
    texts = texts,
    embedding = embedding_function,
    table = "state_union",
    db_file = "demo.db"
)

# First, we will do a simple retrieval using similarity search
# Query
question = "Who won the 2024 Olympics men's speed 100m ? Response with short answer."
data = db.similarity_search(question)
print(data[0].page_content)

# LLM
from langchain_ollama import OllamaLLM
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
llm = OllamaLLM(
    model = "llama3.1",
    verbose = True,
    callbacks = CallbackManager([StreamingStdOutCallbackHandler()]),
)

# QA chain
from langchain.chains import RetrievalQA
from langchain import hub
# LangChain Hub is a repository of LangChain prompts shared by the community
QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever = db.as_retriever(), 
    chain_type_kwargs = {"prompt": QA_CHAIN_PROMPT},
)

result = qa_chain.invoke({"query": question})


