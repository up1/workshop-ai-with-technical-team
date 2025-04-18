from caching import get_from_cache, store_in_cache
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def get_response(query):
    cached_response = get_from_cache(query)
    if cached_response:
        print(f"Cache hit for query: {query}")
        return cached_response
    else:
        print(f"Cache miss for query: {query}")
        # Simulate a call to an LLM
        response = call_llm(query)
        store_in_cache(query, response)
        return response

def call_llm(query):
    llm = ChatOpenAI(model="gpt-4")
    prompt = PromptTemplate.from_template("As assistant, I will answer the question in {output_language}.\n\n{input}\n\nAnswer:")
    chain = prompt | llm
    response = chain.invoke(
        {
            "output_language": "thai",
            "input": query,
        }
    )
    return response.content

if __name__ == "__main__":
    print("========== 1st call ==============")
    response1 = get_response("What is semantic caching ?")
    print(response1)

    print("========== 2nd call ==============")
    response2 = get_response("Detail of semantic caching ?")
    print(response2)
    
