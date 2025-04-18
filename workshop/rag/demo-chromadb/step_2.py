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
print("Size of chunk:", splits.__len__())
for idx, text in enumerate(splits):
    text.metadata["id"] = idx

# Show the first 5 splits
for split in splits[:5]:
    print("ID:", split.metadata["id"])
    # remove whitespace between the text
    # and the text content
    # remove the leading and trailing whitespace
    # and the text content
    # split.page_content = split.page_content.replace("\n", " ")
    # split.page_content = split.page_content.replace("\r", " ")
    # split.page_content = split.page_content.replace("\t", " ")
    # split.page_content = split.page_content.strip()
    print(split.page_content)
    print("=====================")
