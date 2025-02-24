from openai import OpenAI
import base64

model = "gemini-2.0-flash" # "gpt-4o-mini"
client = OpenAI(
    api_key="your-api-key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def image_to_text_from_url(image_url):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract all the text content from this image."},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

def image_to_text_from_base64(image_base64):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Extract all the text content from this image thoroughly and accurately. Ensure that no lines, words, or parts of the content are missed, even if the text is faint, small, or near the edges. The text may include headings, paragraphs, or lists and could appear in various fonts, styles, or layouts. Carefully preserve the reading order and structure as it appears in the image. Double-check for any skipped lines or incomplete content, and extract every visible text element, ensuring completeness across all sections. This is crucial for the task's accuracy."
                        )
                    },
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"}
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(response)
    return response.choices[0].message.content

# Example usage:
if __name__ == "__main__":
    local_image_path = "image.png"
    image_base64 = image_to_base64(local_image_path)
    print("\nExtracted text from Base64:")
    extracted_text = image_to_text_from_base64(image_base64)
    print(extracted_text)