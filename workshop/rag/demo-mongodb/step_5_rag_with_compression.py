from step_2_embedding import get_embedding
from step_3_save_to_mongodb import get_mongo_client
from step_4_rag_with_mongodb import vector_search
import os
import openai
import pprint

# Configurations
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = "demo_employees"
COLLECTION_NAME = "employees"
OPEN_AI_MODEL = "gpt-4o"

from llmlingua import PromptCompressor

llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank",
    model_config={"revision": "main"},
    use_llmlingua2=True,
    device_map="cpu" # change to 'cuda' if gpu is availabe on device
)

def compress_query_prompt(context):
  compressed_prompt = llm_lingua.compress_prompt(
    str(context),
    rate=0.33,
    force_tokens=["!", ".", "?", "\n"],
    drop_consecutive=True,
  )

  print("------")
  print(compressed_prompt)
  print("-------")

  return compressed_prompt

def handle_user_query_with_compression(query, collection):

  get_knowledge = vector_search(query, collection)

  # Concatenate the search results to reflect the employee profile
  search_result = ''

  for result in get_knowledge:
      employee_profile = f"""
      Employee ID: {result['employee_id']}
      Name: {result['first_name']} {result['last_name']}
      Job Details: Title - {result['job_details']['job_title']}
      """
      search_result += employee_profile + "\n"

  # Prepare information for compression
  query_info = {
    'demonstration_str': search_result,  # Results from information retrieval process
    'instruction': "Write a high-quality answer for the given question using only the provided search results.",
    'question': query
  }

  # Compress the query prompt
  compressed_prompt = compress_query_prompt(query_info)

  prompt =  f"Answer this user query: {query} with the following context:\n{compressed_prompt}"
  print("Compressed Prompt:\n")
  pprint.pprint(prompt)

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
    response, search_result = handle_user_query_with_compression(user_query, collection)
    print("Response from the system:\n")
    print(response)