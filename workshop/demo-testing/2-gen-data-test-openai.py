import schemathesis
from openai import OpenAI

# Initialize OpenAI client
model = "gpt-4o"
client = OpenAI()

# Read OpenAPI specificatin from file
api_spec = schemathesis.from_path("openapi.yml")


# Generate mock data for the given prompt
def generate_mock_data(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a automation tester."},
            {"role": "user", "content": """
             A good list of test cases should include cases for:
                - all the possible status codes
                - varios request parameters, request headers
                - response body content
                - positive, negative and edge cases
             """},
            {"role": "user", "content": "Context : \n\n Swagger specification below:\n\n {api_spec}"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()


# Generate mock data for the given endpoint
product_id = 1
prompt = f"To help test GET /products/:id API (get product detail), list diverse scenarios which post /products/:id API (get product detail) should handle. Format them as ordered list, one case per item."
mock_response = generate_mock_data(prompt)
print(mock_response)