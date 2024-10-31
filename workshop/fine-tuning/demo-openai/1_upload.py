from openai import OpenAI
client = OpenAI()


response = client.files.create(
  file=open("training-dataset.jsonl", "rb"),
  purpose="fine-tune"
)

print(response)