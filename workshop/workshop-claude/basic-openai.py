import os
from openai import OpenAI

client = OpenAI(
    api_key= os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://api.anthropic.com/v1/"  # Anthropic's API endpoint
)

response = client.chat.completions.create(
    model="claude-opus-4-1-20250805", # Anthropic model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"}
    ],
)

print(response.choices[0].message.content)