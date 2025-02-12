from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate
from utils import format_docs

def create_rag_chain(retriever):
    template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know". Use three sentences maximum and keep the answer concise.

Question: {question} 
Context: {context} 
Answer:
"""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    prompt = PromptTemplate.from_template(template=template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain
