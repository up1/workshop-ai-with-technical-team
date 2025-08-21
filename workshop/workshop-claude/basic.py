import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message)