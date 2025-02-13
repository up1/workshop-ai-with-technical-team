from anthropic import Anthropic
import sqlite3

# Set up the Anthropic API client
client = Anthropic()
MODEL_NAME = "claude-3-opus-20240229"

def ask_claude(query, schema):
    prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? 
Only output the SQL query and nothing else.

Question: {query}
"""

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        messages=[{
            "role": 'user', "content": prompt
        }]
    )
    return response.content[0].text

def main():
    # Connect to the existing database
    conn = sqlite3.connect("test_db.db")
    cursor = conn.cursor()

    # Get the database schema
    schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
    schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
    print("Database Schema:")
    print(schema_str)

    # Example natural language question
    question = "List all employees in the Sales department with a salary greater than 55000."
    print("\nQuestion:", question)
    
    # Send the question to Claude and get the SQL query
    sql_query = ask_claude(question, schema_str)
    print("\nGenerated SQL Query:")
    print(sql_query)

    # Execute the query and show results
    try:
        results = cursor.execute(sql_query).fetchall()
        print("\nQuery Results:")
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print("Error executing query:", e)
    
    conn.close()

if __name__ == "__main__":
    main()