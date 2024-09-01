import os
from openai import OpenAI

model = "gpt-4o"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
prompt = """Answer the question as truthfully as possible, and if you're unsure of the answer, say "Sorry, I don't know".

Q: Who won the 2024 Olympics men's speed 100m
A:"""

chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

print(chat_completion.choices[0].message.content)