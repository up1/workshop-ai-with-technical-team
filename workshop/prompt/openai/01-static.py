import os
from openai import OpenAI

model = "gpt-4o"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

prompt = "Who won the 2020 Olympics men's speed 100m"

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