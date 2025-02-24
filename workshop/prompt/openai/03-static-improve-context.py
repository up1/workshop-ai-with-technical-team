import os
from openai import OpenAI

model = "gpt-4o"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
prompt = """Answer the question as truthfully as possible, and if you're unsure of the answer, say "Sorry, I don't know".

Context:
The men's 100 metres event at the 2024 Summer Olympics took place on 3 August 
and 4 August at the Stade de France in Paris. Noah Lyles won the gold medal, 
setting a new personal best in the 100m and giving the United States 
its first victory in the event since 2004.

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