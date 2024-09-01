import os
from openai import OpenAI

# Read context from a text file
with open('context.txt', 'r') as file:
    context = file.read()

# Define the model and client
model = "gpt-4o"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create the prompt using the read context
prompt = f"""Answer the question as truthfully as possible, and if you're unsure of the answer, say "Sorry, I don't know".

Context:
{context}

Q: Who won the 2024 Olympics men's speed 100m
A:"""

# Generate the completion
chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

# Print the result
print(chat_completion.choices[0].message.content)