from step_1_download_data import pdf_to_base64_pngs, process_pdf
from concurrent.futures import ThreadPoolExecutor
from anthropic import Anthropic
import os

# Set up the Anthropic API client
client = Anthropic()
MODEL_NAME_HAIKU = "claude-3-haiku-20240307"
MODEL_NAME_OPUS = "claude-3-opus-20240229"

# User's question
QUESTION = "How did Apple's net sales change quarter to quarter in the 2023 financial year and what were the key contributors to the changes?"

def generate_opus_prompt(question):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"Based on the following question, please generate a specific prompt for an LLM sub-agent to extract relevant information from an earning's report PDF. Each sub-agent only has access to a single quarter's earnings report. Output only the prompt and nothing else.\n\nQuestion: {question}"}
            ]
        }
    ]

    response = client.messages.create(
        model=MODEL_NAME_OPUS,
        max_tokens=2048,
        messages=messages
    )

    return response.content[0].text

def extract_info(pdf_path, prompt):
    base64_encoded_pngs = pdf_to_base64_pngs(pdf_path)
    
    messages = [
        {
            "role": "user",
            "content": [
                *[{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": base64_encoded_png}} for base64_encoded_png in base64_encoded_pngs],
                {"type": "text", "text": prompt}
            ]
        }
    ]
    
    response = client.messages.create(
        model=MODEL_NAME_HAIKU,
        max_tokens=2048,
        messages=messages
    )
    
    return response.content[0].text, pdf_path

def process_pdf(pdf_path):
    return extract_info(pdf_path, generate_opus_prompt(QUESTION))


# main function
if __name__ == "__main__":

    # List file within the folder and return absolute path
    folder = "./images"
    pdf_paths = [os.path.join(folder, pdf_path) for pdf_path in os.listdir(folder) if pdf_path.endswith(".pdf")]
    
    # Process the PDFs concurrently
    with ThreadPoolExecutor() as executor:
        extracted_info_list = list(executor.map(process_pdf, pdf_paths))

    extracted_info = ""
    # Display the extracted information from each model call
    for info in extracted_info_list:
        extracted_info += "<info quarter=\"" + info[1].split("/")[-1].split("_")[1] + "\">" + info[0] + "</info>\n"
    print(extracted_info)

    # Save the extracted information to a file
    with open("extracted_info.txt", "w") as file:
        file.write(extracted_info)
