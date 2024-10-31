from IPython.display import Markdown, display
from openai import OpenAI
import os

openai_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a great philosopher."},
    {"role": "user", "content": "What is the meaning of life?"}
  ]
)

print(response.choices[0].message.content)