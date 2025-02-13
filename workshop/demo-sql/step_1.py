import sqlite3

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Create a sample table
# Drop if exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create a new table
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
conn.close()

print("Database created successfully with sample data!")