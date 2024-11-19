from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import PromptTemplate
from llama_index.llms.openai import OpenAI

# load data
documents = SimpleDirectoryReader(input_dir="./02-data/").load_data()

# build VectorStoreIndex that takes care of chunking documents
# and encoding chunks to embeddings for future retrieval
index = VectorStoreIndex.from_documents(documents=documents)

# The QueryEngine class is equipped with the generator
# and facilitates the retrieval and generation steps
query_engine = index.as_query_engine()

# Create ChatTemplate for the response
text_qa_template_str = (
    "Context information is"
    " below.\n---------------------\n{context_str}\n---------------------\nUsing"
    " both the context information and also using your own knowledge, answer"
    " the question: {query_str}\n "
    " Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say `I don't know`."
)
text_qa_template = PromptTemplate(text_qa_template_str)

llm = OpenAI(model="gpt-4o")
print(
    index.as_query_engine(
        text_qa_template=text_qa_template,
        llm=llm,
    ).query("abc")
)
