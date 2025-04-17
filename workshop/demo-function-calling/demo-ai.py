# import function from file weather-tool.py
from weather_tool import get_weather
from openai import OpenAI
import json

client = OpenAI()
tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for provided coordinates in celsius.",
    "parameters": {
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]


if __name__ == "__main__":
    # 1. Get the weather for Thailand
    input_messages = [{"role": "user", "content": "What's the weather like in Bangkok, Thailand today?"}]
    response = client.responses.create(
        model="gpt-4.1",
        input=input_messages,
        tools=tools,
    )
    # Print the response
    print(response.output)

    # 2. Execute get_weather function
    tool_call = response.output[0]
    args = json.loads(tool_call.arguments)
    result = get_weather(args["latitude"], args["longitude"])
    # Print the result
    print(f"The current temperature is {result}°C")