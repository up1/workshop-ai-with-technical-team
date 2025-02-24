from langchain.prompts import PromptTemplate
from create_vector import create_client, create_llm
from langchain_community.vectorstores.faiss import FAISS
from langchain_aws import BedrockEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate

QUERY_PROMPT = """
If the question is not relevant to the provided documents, 
respond with "I don't know" or "This question is outside the bounds of the data I am trained on".

Context : {context} 
"""

def create_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", QUERY_PROMPT),
            ("human", "{input}"),
        ]
    )
    return prompt 

def create_qa_chain(question):

    # create client 
    bedrock_client = create_client()

    # load llm
    llm = create_llm(bedrock_client=bedrock_client)

    # create prompt
    prompt = create_prompt()

    # load embeddings and vector store
    bedrock_embeddings=BedrockEmbeddings(model_id='amazon.titan-embed-text-v2:0', client=bedrock_client)
    vector_store = FAISS.load_local('faiss_index', bedrock_embeddings, allow_dangerous_deserialization=True)

    # create chains
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(vector_store.as_retriever(search_type='similarity', search_kwargs={"k":3}), question_answer_chain)
    result = rag_chain.invoke({"input": question})
    return result
    

if __name__ == "__main__":
    result = create_qa_chain("“ซุปเปอร์เฟรนด์ส คืออะไร")
    print(result)
    print("====== Answer =====")
    if "answer" in result:
        print(result["answer"])
    else:
        print("No answer found.")