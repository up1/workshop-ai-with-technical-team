from step_2_embedding import create_employee_string, get_embedding
import pandas as pd
from pymongo.mongo_client import MongoClient
import os

# MongoDB configuration
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = "demo_employees"
COLLECTION_NAME = "employees"

# Connect to MongoDB
def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""

    # gateway to interacting with a MongoDB database cluster
    client = MongoClient(mongo_uri, appname="demo-rag")
    print("Connection to MongoDB successful")
    return client


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

    # 4. Connect to MongoDB
    if not MONGO_URI:
        print("MONGO_URI not set in environment variables")
        exit(1)
    mongo_client = get_mongo_client(MONGO_URI)

    # 5. Create a database and collection
    db = mongo_client.get_database(DATABASE_NAME)
    collection = db.get_collection(COLLECTION_NAME)

    # 6. Insert the data into the collection
    documents = df_employees.to_dict('records')
    collection.delete_many({})
    collection.insert_many(documents)
    print("Data ingestion into MongoDB completed")