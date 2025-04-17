from openai import OpenAI
client = OpenAI()

# Read text from file
text = ""
with open('data.txt', 'r') as file:
    text = file.read()

# Connect to the OpenAI API
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "assistant", "content": "You are a helpful assistant."},
        {"role": "user", "content": text}
    ]
)

# Print the response for caching details
usage = response.usage
print(usage)