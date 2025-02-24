from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

QUERY_PROMPT = """
Role : เป็นพนักงานตอบคำถาม online จากลูกค้า

Instruction :
ให้ทำการตอบถามถามที่อยู่ในส่วนของ context ด้านล่างเท่านั้น
ถ้าไม่พบคำตอบ ให้ทำการตอบกลับไปว่า "ทำการติดต่อมาได้ที่เบอร์ 086-444-4444"

Context : FAQ ของร้านขายเครื่องสำอางค์ออนไลน์
{context}
"""

LLM = ChatOpenAI(model="gpt-4o-mini")

# Read data from the file and split it to generate vectorstore
def read_data_and_convert_to_vector(file_path):
    loader = TextLoader(file_path)
    content = loader.load_and_split()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(content, embeddings)
    return vectorstore

# Generate response using OpenAI
def generate_response(question, retriever):
    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", QUERY_PROMPT),
        ("human", "{input}"),
    ]
)
    question_answer_chain = create_stuff_documents_chain(LLM, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    result = rag_chain.invoke({"input": question})
    return result

if __name__ == "__main__":
    # Path to your text file
    file_path = 'faq.txt'
    
    # Read data from the file and convert it to vectorstore
    vectorstore = read_data_and_convert_to_vector(file_path)
    
    # Convert vectorstore to retriever
    if vectorstore is not None:
        retriever = vectorstore.as_retriever()
    else:
        retriever = None
    
    # Generate response
    prompt = "สีเหลืองคือสีอะไร"
    response = generate_response(prompt, retriever)
    print(response)
    print("============ Answer ===========")
    print(response["answer"])