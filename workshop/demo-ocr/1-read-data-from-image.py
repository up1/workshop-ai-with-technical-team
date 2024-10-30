from PIL import Image
import pytesseract
from langchain_openai import OpenAI
from langchain.schema import HumanMessage
import json
import base64

# Load the image file
image_path = 'kbank.jpg'
image = Image.open(image_path)

# Extract text from the image using pytesseract
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)

# Encode the image in base64
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Initialize OpenAI API with LangChain
llm = OpenAI()

# Create the prompt with the extracted text and encoded image
prompt = [
    HumanMessage(content="Return in json format"),
    HumanMessage(content=f"Encoded image: {extracted_text}")
]

# Process the prompt using OpenAI's API
response = llm.invoke(prompt)

# Convert the response to JSON format
response_json = json.loads(response)

print(response)
print(response_json.get("amount"))
