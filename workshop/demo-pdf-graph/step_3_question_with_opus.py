from anthropic import Anthropic

# Set up the Anthropic API client
client = Anthropic()
MODEL_NAME_OPUS = "claude-3-opus-20240229"

# User's question
QUESTION = "How did Apple's net sales change quarter to quarter in the 2023 financial year and what were the key contributors to the changes?"

# Read data from file
extracted_info = ""
with open("extracted_info.txt", "r") as file:
    extracted_info = file.read()

# Prepare the messages for the powerful model
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": f"Based on the following extracted information from Apple's earnings releases, please provide a response to the question: {QUESTION}\n\nAlso, please generate Python code to create bar chart using the matplotlib library  to accompany your response. Enclose the code within <code> tags.\n\nExtracted Information:\n{extracted_info}"}
        ]
    }
]

# Generate the matplotlib code using the powerful model
response = client.messages.create(
    model=MODEL_NAME_OPUS,
    max_tokens=4096,
    messages=messages
)

# Extract the generated response and the matplotlib code
def extract_code_and_response(response):
    start_tag = "<code>"
    end_tag = "</code>"
    start_index = response.find(start_tag)
    end_index = response.find(end_tag)
    if start_index != -1 and end_index != -1:
        code = response[start_index + len(start_tag):end_index].strip()
        non_code_response = response[:start_index].strip()
        return code, non_code_response
    else:
        return None, response.strip()

# Display the generated response
generated_response = response.content[0].text
print("Generated Response:")
print(generated_response)

# Extract the matplotlib code and the non-code response
matplotlib_code, non_code_response = extract_code_and_response(generated_response)
print(non_code_response)
if matplotlib_code:
    # Execute the extracted matplotlib code
    exec(matplotlib_code)
else:
    print("No matplotlib code found in the response.")
