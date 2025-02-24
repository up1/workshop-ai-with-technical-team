import sqlite3

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Step 2 :: Connect to the vector database
sql_query = "SELECT * FROM employees"
results = cursor.execute(sql_query).fetchall()

# Step 3 :: Save the data to a pandas DataFrame
import pandas as pd
df_employees = pd.DataFrame(results, columns=["id", "name", "job_title", "department", "salary", "office_locations"])
print("Original employees from database:")
print(df_employees.head(), "\n")

# Close the connection
conn.close()


# Step 4 :: Create a new column in the DataFrame that contains a string representation of the employee
def create_employee_string(employee):
    return f"Employee information \n{employee['name']} is a {employee['job_title']} in the {employee['department']} department and working at {employee['office_locations']}."

df_employees['employee_string'] = df_employees.apply(create_employee_string, axis=1)
pd.set_option('display.max_colwidth', None)
print("Employee for search:")
print(df_employees[['id', 'employee_string']].head())

# Step 5 :: Save the data to a vector database
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_core.documents import Document
documents = df_employees['employee_string'].tolist()

# Convert to Document objects
documents_with_content = [Document(page_content=doc) for doc in documents]
print("First two documents:")
print(documents_with_content[:2])

# Save the vectorstore to disk
vectorstore = Chroma.from_documents(
    documents=documents_with_content, 
    embedding=OpenAIEmbeddings(),
    persist_directory="employee_db",
    collection_name="demo_employee"
)
print("Vectorstore saved to disk")