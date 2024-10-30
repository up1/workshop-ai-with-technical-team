import os
import openai
import pandas as pd
import random

# OpenAI API Key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
OPEN_AI_MODEL = "gpt-4o"
OPEN_AI_EMBEDDING_MODEL = "text-embedding-3-small"
OPEN_AI_EMBEDDING_MODEL_DIMENSION = 1536

# Define a list of job titles and departments for variety
job_titles = [
    "Software Engineer", "Senior Software Engineer", "Data Scientist", "Product Manager",
    "Project Manager", "UX Designer", "QA Engineer", "DevOps Engineer", "CTO", "CEO"
]
departments = [
    "IT", "Engineering", "Data Science", "Product", "Project Management", "Design",
    "Quality Assurance", "Operations", "Executive"
]

# Define a list of office locations
office_locations = [
    "Chicago Office", "New York Office", "London Office", "Berlin Office", "Tokyo Office",
    "Sydney Office", "Toronto Office", "San Francisco Office", "Paris Office", "Singapore Office"
]

# Define a function to create a random employee entry
def create_employee(employee_id, first_name, last_name, job_title, department, manager_id=None):
    return {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": random.choice(["Male", "Female"]),
        "date_of_birth": f"{random.randint(1950, 2000)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
        "address": {
            "street": f"{random.randint(100, 999)} Main Street",
            "city": "Springfield",
            "state": "IL",
            "postal_code": "62704",
            "country": "USA"
        },
        "contact_details": {
            "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
            "phone_number": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        },
        "job_details": {
            "job_title": job_title,
            "department": department,
            "hire_date": f"{random.randint(2000, 2022)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
            "employment_type": "Full-Time",
            "salary": random.randint(50000, 250000),
            "currency": "USD"
        },
        "work_location": {
            "nearest_office": random.choice(office_locations),
            "is_remote": random.choice([True, False])
        },
        "reporting_manager": manager_id,
        "skills": random.sample(
            ["JavaScript", "Python", "Node.js", "React", "Django", "Flask", "AWS", "Docker", "Kubernetes", "SQL"], 4
        ),
        "performance_reviews": [
            {
                "review_date": f"{random.randint(2020, 2023)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
                "rating": round(random.uniform(3, 5), 1),
                "comments": random.choice([
                    "Exceeded expectations in the last project.",
                    "Consistently meets performance standards.",
                    "Needs improvement in time management.",
                    "Outstanding performance and dedication."
                ])
            },
            {
                "review_date": f"{random.randint(2019, 2022)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
                "rating": round(random.uniform(3, 5), 1),
                "comments": random.choice([
                    "Exceeded expectations in the last project.",
                    "Consistently meets performance standards.",
                    "Needs improvement in time management.",
                    "Outstanding performance and dedication."
                ])
            }
        ],
        "benefits": {
            "health_insurance": random.choice(["Gold Plan", "Silver Plan", "Bronze Plan"]),
            "retirement_plan": "401K",
            "paid_time_off": random.randint(15, 30)
        },
        "emergency_contact": {
            "name": f"{random.choice(['Jane', 'Emily', 'Michael', 'Robert'])} {random.choice(['Doe', 'Smith', 'Johnson'])}",
            "relationship": random.choice(["Spouse", "Parent", "Sibling", "Friend"]),
            "phone_number": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        },
        "notes": random.choice([
            "Promoted to Senior Software Engineer in 2020.",
            "Completed leadership training in 2021.",
            "Received Employee of the Month award in 2022.",
            "Actively involved in company hackathons and innovation challenges."
        ])
    }

# main function
if __name__ == "__main__":

    # Generate 10 employee entries
    employees = [
        create_employee("E123456", "John", "Doe", "Software Engineer", "IT", "M987654"),
        create_employee("E123457", "Jane", "Doe", "Senior Software Engineer", "IT", "M987654"),
        create_employee("E123458", "Emily", "Smith", "Data Scientist", "Data Science", "M987655"),
        create_employee("E123459", "Michael", "Brown", "Product Manager", "Product", "M987656"),
        create_employee("E123460", "Sarah", "Davis", "Project Manager", "Project Management", "M987657"),
        create_employee("E123461", "Robert", "Johnson", "UX Designer", "Design", "M987658"),
        create_employee("E123462", "David", "Wilson", "QA Engineer", "Quality Assurance", "M987659"),
        create_employee("E123463", "Chris", "Lee", "DevOps Engineer", "Operations", "M987660"),
        create_employee("E123464", "Sophia", "Garcia", "CTO", "Executive", None),
        create_employee("E123465", "Olivia", "Martinez", "CEO", "Executive", None)
    ]

    # Convert to DataFrame
    df_employees = pd.DataFrame(employees)

    # Save DataFrame to CSV
    csv_file_employees = 'employees.csv'
    df_employees.to_csv(csv_file_employees, index=False)

    print(f"Employee data has been saved to {csv_file_employees}")
    print(df_employees.head())
