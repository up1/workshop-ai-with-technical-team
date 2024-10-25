from anthropic import Anthropic
import sqlite3

# Set up the Anthropic API client
client = Anthropic()
MODEL_NAME = "claude-3-opus-20240229"

# Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

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

# Define a function to send a query to Claude and get the response
def ask_claude(query, schema):
    prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? Only output the SQL query and nothing else.

Question: {query}
"""

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    )
    return response.content[0].text

# Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
print(schema_str)


# Example natural language question
question = "What are the names and salaries of employees in the Engineering department?"
# Send the question to Claude and get the SQL query
sql_query = ask_claude(question, schema_str)
print(sql_query)