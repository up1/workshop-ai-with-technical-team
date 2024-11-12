import os
import openai

# Read text from file
text = ""
with open('data.txt', 'r') as file:
    text = file.read()

# Connect to the OpenAI API
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text}
    ]
)

# Print the response for caching details
usage = response.usage
print(usage)