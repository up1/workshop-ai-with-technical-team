from caching import get_from_cache, store_in_cache

def get_response(query):
    cached_response = get_from_cache(query)
    if cached_response:
        return cached_response
    else:
        # Simulate a call to an LLM
        response = call_llm(query)
        store_in_cache(query, response)
        return response

def call_llm(query):
    # Simulate a call to an LLM
    # In a real-world scenario, this would be replaced with actual LLM call
    return f"Response for query: {query}"

if __name__ == "__main__":
    print("========== 1st call ==============")
    response1 = get_response("What is semantic caching ?")
    print(response1)

    print("========== 2nd call ==============")
    response2 = get_response("Detail of semantic caching ?")
    print(response2)
    
