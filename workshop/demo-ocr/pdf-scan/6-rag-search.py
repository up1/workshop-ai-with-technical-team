from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain


QUERY_PROMPT = """
Instructions: Answer the following question based on the context provided with short answer.
and if the answer is not contained within the text below, say "I don't know
Context : {context}
"""

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Generate response using OpenAI
def generate_response(retriever, question):
    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", QUERY_PROMPT),
        ("human", "{input}"),
    ]
)
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    result = rag_chain.invoke({"input": question})
    return result

if __name__ == "__main__":
    # Question from user
    question = "ประกาศในปีอะไร"

    # 1. Load embeddings and the FAISS index
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("data.faiss", embeddings, allow_dangerous_deserialization=True)

    # 2. Search for relevant data
    relevant_data = db.similarity_search_with_score(question)
    if len(relevant_data) == 0:
        print("No documents found")
        exit()

    # 2.2 filter out the relevant data with lesss than 0.3 similarity score
    relevant_data = [data for data in relevant_data if data[1] > 0.3]
    if len(relevant_data) == 0:
        print("No relevant documents found > 0.5 similarity score")
        exit()

    # 2.3 Create a new FAISS index with the relevant data
    relevant_data_db = FAISS.from_documents([data[0] for data in relevant_data], embeddings)
    
    # 3. Generate response
    response = generate_response(relevant_data_db.as_retriever() , question)

    # Print the response
    print(response)
    print(response["answer"])