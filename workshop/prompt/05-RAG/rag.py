from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

# Output parser will split the LLM result into a list of queries
class LineListOutputParser(BaseOutputParser[List[str]]):
    """Output parser for a list of lines."""

    def parse(self, text: str) -> List[str]:
        lines = text.strip().split("\n")
        return list(filter(None, lines))  # Remove empty lines

# Read data from the file and split it to generate vectorstore
def read_data_and_convert_to_vector(file_path):
    loader = TextLoader(file_path)
    content = loader.load_and_split()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(content, embeddings)
    return vectorstore

# Generate response using OpenAI
def generate_response(prompt, retriever):
    QUERY_PROMPT = PromptTemplate(
        template="""
        Answer the question as truthfully as possible, and if you're unsure of the answer, 
        say "Sorry, I don't know".
        """
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=100)
    llm_chain = QUERY_PROMPT | llm | LineListOutputParser()
    multipleRetriver = MultiQueryRetriever(
        retriever=retriever, 
        llm_chain=llm_chain, 
        parser_key="lines")
    docs = multipleRetriver.invoke(prompt)
    return docs

if __name__ == "__main__":
    # Path to your text file
    file_path = 'context.txt'
    
    # Read data from the file and convert it to vectorstore
    vectorstore = read_data_and_convert_to_vector(file_path)

    # Convert vectorstore to retriever
    if vectorstore is not None:
        retriever = vectorstore.as_retriever()
    else:
        retriever = None
    
    # Generate response
    prompt = "Who won the 2024 Olympics men's speed 100m"
    response = generate_response(prompt, retriever)
    print(response)
    print(response[0].page_content)