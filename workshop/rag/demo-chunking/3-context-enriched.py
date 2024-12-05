from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from openai import OpenAI

#Loading text from Wikipedia page
url="https://en.wikipedia.org/wiki/FIFA_World_Cup"
loader = AsyncHtmlLoader(url)
data = loader.load()
html2text = Html2TextTransformer()
data_transformed = html2text.transform_documents(data)
document_text = data_transformed[0].page_content

# Generating summary of the text using GPT-4o-mini model
summary_prompt = f"Summarize the given document in a single paragraph\ndocument: {document_text}"
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages= [
    {"role": "user", "content": summary_prompt}
  ]
)
summary=response.choices[0].message.content
print(summary)

# Creating Chunks with Recursive Character Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
chunk_size=1000,
chunk_overlap=200)
chunks=text_splitter.split_text(data_transformed[0].page_content)

# Enriching Chunks with Summary Data
context_enriched_chunks = [summary + "\n" + chunk for chunk in chunks]

# Creating embeddings and storing in FAISS index
embedding = OpenAIEmbeddings()
vector_store = FAISS.from_texts(context_enriched_chunks, embedding)
vector_store.save_local("fifa_world_cup.faiss")