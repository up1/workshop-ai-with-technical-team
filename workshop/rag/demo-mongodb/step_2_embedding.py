import openai
import pandas as pd
import ast
import os

# OpenAI API Key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
OPEN_AI_MODEL = "gpt-4o"
OPEN_AI_EMBEDDING_MODEL = "text-embedding-3-small"
OPEN_AI_EMBEDDING_MODEL_DIMENSION = 1536

def create_employee_string(employee):
    # convert string to dictionary
    employee['job_details'] = ast.literal_eval(employee['job_details'])
    employee['performance_reviews'] = ast.literal_eval(employee['performance_reviews'])
    employee['skills'] = ast.literal_eval(employee['skills'])
    employee['work_location'] = ast.literal_eval(employee['work_location'])

    job_details = f"{employee['job_details']['job_title']} in {employee['job_details']['department']}"
    skills = ", ".join(employee['skills'])
    performance_reviews = " ".join([f"Rated {review['rating']} on {review['review_date']}: {review['comments']}" for review in employee['performance_reviews']])
    basic_info = f"{employee['first_name']} {employee['last_name']}, {employee['gender']}, born on {employee['date_of_birth']}"
    work_location = f"Works at {employee['work_location']['nearest_office']}, Remote: {employee['work_location']['is_remote']}"
    notes = employee['notes']

    return f"{basic_info}. Job: {job_details}. Skills: {skills}. Reviews: {performance_reviews}. Location: {work_location}. Notes: {notes}"


def get_embedding(text):
    """Generate an embedding for the given text using OpenAI's API."""

    # Check for valid input
    if not text or not isinstance(text, str):
        return None

    try:
        # Call OpenAI API to get the embedding
        embedding = openai.embeddings.create(
            input=text,
            model=OPEN_AI_EMBEDDING_MODEL, dimensions=OPEN_AI_EMBEDDING_MODEL_DIMENSION).data[0].embedding
        return embedding
    except Exception as e:
        print(f"Error in get_embedding: {e}")
        return None


# main function
if __name__ == "__main__":
    # 1. Read the data from the CSV file to dictionary
    df_employees = pd.read_csv('employees.csv')

    # 2. Apply the function to all employees
    df_employees['employee_string'] = df_employees.apply(create_employee_string, axis=1)
        

    # 3. Apply the function to generate embeddings for all employees with error handling
    try:
        df_employees['embedding'] = df_employees['employee_string'].apply(get_embedding)
        print("Embeddings generated for employees")
    except Exception as e:
        print(f"Error applying embedding function to DataFrame: {e}")

    print(df_employees.head())