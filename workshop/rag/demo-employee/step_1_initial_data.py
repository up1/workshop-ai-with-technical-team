import sqlite3

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
        job_title TEXT,
        department TEXT,
        salary INTEGER,
        office_locations TEXT
    )
""")

# Insert sample data
sample_data = [
    (1, "John Doe", "Software Engineer", "IT", 50000, "Chicago Office"),
    (2, "Jane Doe", "Data Scientist", "Data Science", 60000, "New York Office"),
    (3, "Alice Smith", "Product Manager", "Product", 70000, "London Office"),
    (4, "Bob Johnson", "Project Manager", "Project Management", 80000, "Berlin Office"),
    (5, "Charlie Brown", "UX Designer", "Design", 60000, "Tokyo Office"),
    (6, "David Lee", "QA Engineer", "Quality Assurance", 50000, "Sydney Office"),
    (7, "Eve Wong", "DevOps Engineer", "Operations", 55000, "Toronto Office"),
    (8, "Frank Chen", "CTO", "Executive", 90000, "San Francisco Office"),
    (9, "Grace Kim", "CEO", "Executive", 100000, "Paris Office"),
    (10, "Henry Wu", "Senior Software Engineer", "Engineering", 75000, "Singapore Office")
    
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", sample_data)
conn.commit()

# Query the data
sql_query = "SELECT * FROM employees"
results = cursor.execute(sql_query).fetchall()
print("\nAll employees in Database:")
for row in results:
    print(row)

# Close the connection
conn.close()