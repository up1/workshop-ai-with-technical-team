import base64

import anthropic

# Read image file
image_slip = "bank-slip.png"
image_media_type = "image/png"

with open(image_slip, "rb") as image_file:
    image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")

# Prompt template
prompt_template = """
You are a helpful assistant. Analyze the image and provide a detailed description.

Output in JSON format only and not show other information
"""

# Create message and send to Claude
message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": prompt_template
                }
            ],
        }
    ],
)

# Print message 
print(message)
print(message.content[0].text)