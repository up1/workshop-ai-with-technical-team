from openai import OpenAI
client = OpenAI()


response = client.fine_tuning.jobs.create(
  training_file="file-VkXSUBKxYwP6ygmg8EdYBZ8A", # Change to your file
  model="gpt-4o-2024-08-06"
)

print(response)
