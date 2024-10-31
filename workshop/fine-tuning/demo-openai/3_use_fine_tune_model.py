from openai import OpenAI
import os

openai_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="ft:gpt-4o-2024-08-06:personal::AOO5WPV0", # Change to your model
  messages=[
    {"role": "system", "content": "You are a teaching assistant for Machine Learning. You should help to user to answer on his question."},
    {"role": "user", "content": "What is a loss function?"}
  ]
)

print(response.choices[0].message.content)