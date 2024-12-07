import sqlite3
from openai import OpenAI

# Constants
OPENAI_BASE_URL = 'http://localhost:11434/v1'
OPENAI_API_KEY = 'ollama'  # Required but unused
OPENAI_MODEL_NAME = "llama3.2:1b"
DATABASE_NAME = "test_db.db"
EMPLOYEES_TABLE_NAME = "employees"

# Initialize the OpenAI client
openai_client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)

def setup_database():
    """Set up the SQLite database and populate it with sample data."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {EMPLOYEES_TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary INTEGER
        )
    """)

    # Sample data
    sample_employees = [
        (1, "John Doe", "Sales", 50000),
        (2, "Jane Smith", "Engineering", 75000),
        (3, "Mike Johnson", "Sales", 60000),
        (4, "Emily Brown", "Engineering", 80000),
        (5, "David Lee", "Marketing", 55000)
    ]

    # Insert sample data
    cursor.executemany(f"INSERT OR IGNORE INTO {EMPLOYEES_TABLE_NAME} VALUES (?, ?, ?, ?)", sample_employees)
    connection.commit()
    return connection, cursor

def fetch_database_schema(cursor):
    """Fetch the database schema as a formatted string."""
    table_schema_info = cursor.execute(f"PRAGMA table_info({EMPLOYEES_TABLE_NAME})").fetchall()
    schema_description = f"CREATE TABLE {EMPLOYEES_TABLE_NAME.upper()} (\n"
    schema_description += "\n".join([f"    {column[1]} {column[2]}" for column in table_schema_info])
    schema_description += "\n)"
    return schema_description

def generate_sql_query(natural_language_query, database_schema):
    """Send a natural language query to the OpenAI client and return the generated SQL query."""
    response = openai_client.chat.completions.create(
        model=OPENAI_MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant to generate SQL from database."},
            {"role": "user", "content": f"Database schema: {database_schema}"},
            {"role": "user", "content": "Given this schema, can you output a SQL query to answer the following question? Only output the SQL query and nothing else."},
            {"role": "user", "content": natural_language_query}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    """Main function to set up the database, retrieve the schema, and query OpenAI for SQL generation."""
    # Initialize database
    connection, cursor = setup_database()

    try:
        # Retrieve database schema
        database_schema = fetch_database_schema(cursor)
        print("Database Schema:")
        print(database_schema)

        # Example natural language question
        user_question = "What are the names and salaries of employees in the Engineering department?"
        print(f"\nUser Question: {user_question}")

        # Generate SQL query from the natural language question
        generated_sql_query = generate_sql_query(user_question, database_schema)
        print(f"Generated SQL Query:\n{generated_sql_query}")

        # Execute the generated SQL query and display results
        cursor.execute(generated_sql_query)
        query_results = cursor.fetchall()
        print("\nQuery Results:")
        for result in query_results:
            print(result)

    finally:
        # Close database connection
        connection.close()

if __name__ == "__main__":
    main()
