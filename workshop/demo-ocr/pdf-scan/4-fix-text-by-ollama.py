import ollama

def generate_prompt(prompt, chart_type, direction):
    # Preset instruction messages for the model
    messages = [
        {
            "role": "user",
            "content": "You are a bot that to check and fix data with thai language.",
        },
        {
            "role": "user",
            "content": "Do not provide any additional information or notes.",
        },
    ]

    # Generate prompt using OpenAI model
    prompt_formatted = f"""
    ทำการแก้ไขให้ถูกต้อง ข้อมูลที่เป็นตัวย่อ ยังให้เก็บไว้ และเพิ่มคำเต็มด้วย โดยใช้ข้อมูลด้านล่าง: 
    {prompt}
    """

    # Add prompt to messages
    messages.append({"role": "user", "content": prompt_formatted})

    return messages


# Generate response using OpenAI model
def SendChatRequest(prompt, chart_type, direction):

    # Assemble the prompt
    full_prompt = generate_prompt(prompt, chart_type, direction)

    # Send prompt to Ollama server
    client = ollama.Client(host='http://143.198.197.152:11434')
    response = client.chat(
        model="llama3.2:3b", messages=full_prompt
    )
    response = response['message']['content']
    response = response.replace("```", "")
    return response

# Example usage

# 1. read data from text file
data = ""
with open('page_1.txt', 'r') as file:
    data = file.read()

# 2. send data to OpenAI
response = SendChatRequest(data, "table", "vertical")
print(response)

# 3. write response to text file
with open('page_1_fixed_ollama.txt', 'w') as file:
    file.write(response)
