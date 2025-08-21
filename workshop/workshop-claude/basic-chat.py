import os
from openai import OpenAI


def start_chatbot():
    """
    Initializes and runs a multi-turn chat session with the OpenAI API.
    """
    client = OpenAI(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        base_url="https://api.anthropic.com/v1/",  # Anthropic's API endpoint
    )

    # This list acts as the memory, storing the entire conversation.
    # The 'system' message sets the assistant's persona for the whole chat.
    conversation_history = [
        {
            "role": "system",
            "content": "You are a helpful and friendly assistant who is an expert on world history with very short answers.",
        }
    ]

    print(
        "History Expert Chatbot is ready! Ask me anything about history. Type 'quit' to exit."
    )
    print("-" * 60)

    # The main loop for the conversation
    while True:
        # 1. Get user input from the console
        user_input = input("You: ")

        # 2. Provide a way for the user to exit the loop
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("It was a pleasure discussing history with you. Goodbye!")
            break

        # 3. Append the user's new message to the history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # 4. Send the entire conversation history to the OpenAI API
            # This provides the model with the necessary context to have a coherent conversation.
            response = client.chat.completions.create(
                model="claude-opus-4-1-20250805",  # Anthropic model name
                messages=conversation_history,
                max_tokens=10,
                temperature=0.7,  # Adds a bit of creativity to the responses
            )

            # 5. Extract the text content from the assistant's message
            assistant_reply = response.choices[0].message.content
            print(f"Assistant: {assistant_reply}")

            # 6. Append the assistant's reply to the history for the next turn
            conversation_history.append(
                {"role": "assistant", "content": assistant_reply}
            )

        except Exception as e:
            print(f"An error occurred while communicating with the API: {e}")
            # Important: If the API call fails, we remove the last user message
            # to keep the history consistent and allow the user to try again.
            conversation_history.pop()


if __name__ == "__main__":
    start_chatbot()
