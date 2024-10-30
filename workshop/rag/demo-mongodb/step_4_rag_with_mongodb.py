from step_2_embedding import get_embedding
from step_3_save_to_mongodb import get_mongo_client
import os
import openai
import ast

# Configurations
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = "demo_employees"
COLLECTION_NAME = "employees"
OPEN_AI_MODEL = "gpt-4o"

def vector_search(user_query, collection, vector_index="vector_index"):
    # Generate embedding for the user query
    query_embedding = get_embedding(user_query)

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search stage
    vector_search_stage = {
        "$vectorSearch": {
            "index": vector_index, # specifies the index to use for the search
            "queryVector": query_embedding, # the vector representing the query
            "path": "embedding", # field in the documents containing the vectors to search against
            "numCandidates": 150, # number of candidate matches to consider
            "limit": 5 # return top 20 matches
        }
    }

    # Define the aggregate pipeline with the vector search stage and additional stages
    pipeline = [vector_search_stage]

    # Execute the search
    results = collection.aggregate(pipeline)

    return list(results)

def handle_user_query(query, collection):

  get_knowledge = vector_search(query, collection)

  # Concatenate the search results to reflect the employee profile
  search_result = ''

  for result in get_knowledge:
      employee_profile = f"""
      Employee ID: {result['employee_id']}
      Name: {result['first_name']} {result['last_name']}
      Manager: {result['reporting_manager']}
      Job Details: Title - {result['job_details']['job_title']}
      """
      search_result += employee_profile + "\n"

  prompt = "Answer this user query: " + query + " with the following context: " + search_result
  print("Uncompressed Prompt:\n")
  print(prompt)

  completion = openai.chat.completions.create(
      model=OPEN_AI_MODEL,
      messages=[
          {"role": "system", "content": "You are an Human Resource System within a corporate company."},
          {"role": "user", "content": prompt}
      ]
  )

  return (completion.choices[0].message.content), search_result


# main function
if __name__ == "__main__":
    # 1. Connect to MongoDB
    mongo_client = get_mongo_client(MONGO_URI)

    # 2. Create a database and collection
    db = mongo_client.get_database(DATABASE_NAME)
    collection = db.get_collection(COLLECTION_NAME)

    # 3. Handle user queries
    user_query = "Who is the CEO?"
    response, search_result = handle_user_query(user_query, collection)
    print("Response from the system:\n")
    print(response)