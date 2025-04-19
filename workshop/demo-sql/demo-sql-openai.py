from openai import OpenAI
import sqlite3

# Set up the OpenAI API client
client = OpenAI()  # Assumes OPENAI_API_KEY environment variable is set
MODEL_NAME = "gpt-4o"  # Using GPT-4o model, adjust as needed

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Drop if exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create a sample table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
""")

# Insert sample data
sample_data = [
    (1, "John Doe", "Sales", 50000),
    (2, "Jane Smith", "Engineering", 75000),
    (3, "Mike Johnson", "Sales", 60000),
    (4, "Emily Brown", "Engineering", 80000),
    (5, "David Lee", "Marketing", 55000)
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", sample_data)
conn.commit()

# Step 2 :: Define a function to send a query to OpenAI and get the response

# Define a function to send a query to OpenAI and get the response
def ask_openai(query, schema):
    prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? 
Only output the SQL query and nothing else.

Question: {query}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2048
    )
    return response.choices[0].message.content

# Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
print("===== Database Schema =====")
print(schema_str)

# Example natural language question
question = "List all employees in the Sales department with a salary greater than 55000."
# Send the question to OpenAI and get the SQL query
sql_query = ask_openai(question, schema_str)
print("\n===== Generated SQL Query =====")
print(sql_query)

# ```sql
# SELECT * FROM EMPLOYEES WHERE department = 'Sales' AND salary > 55000;
# ```

# remove the comment from the SQL query
sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

# Execute the query and show results
print("\n===== Executing SQL Query =====")
try:
    results = cursor.execute(sql_query).fetchall()
    print("\nQuery Results:")
    for row in results:
        print(row)
except sqlite3.Error as e:
    print("Error executing query:", e)

conn.close()