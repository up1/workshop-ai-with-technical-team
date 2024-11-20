import anthropic

# Read text from file
text = ""
with open('data.txt', 'r') as file:
    text = file.read()

client = anthropic.Anthropic()

response = client.beta.prompt_caching.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=[
      {
        "type": "text",
        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
      },
      {
        "type": "text",
        "text": text,
        "cache_control": {"type": "ephemeral"}
      }
    ],
    messages=[{"role": "user", "content": "Summarize data in one line."}],
)
print(response)
