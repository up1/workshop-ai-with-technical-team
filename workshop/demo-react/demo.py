from langchain_openai import ChatOpenAI
# https://platform.openai.com/docs/api-reference/responses/object#responses/object-temperature
model = ChatOpenAI(model="gpt-4o", temperature=0)
from typing import Literal
from langchain_core.tools import tool

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in chiangmai"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


tools = [get_weather]


# Define the graph
from langgraph.prebuilt import create_react_agent
graph = create_react_agent(model, tools=tools)

# Save the graph
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))

# Run the graph
inputs = {"messages": [("user", "what is the weather in sf")]}
print_stream(graph.stream(inputs, stream_mode="values"))

