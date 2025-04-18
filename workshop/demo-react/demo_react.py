from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o", temperature=0)
from weather_tool import get_weather

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


tools = [get_weather]


# Define the graph
from langgraph.prebuilt import create_react_agent
graph = create_react_agent(model, tools=tools)

# Save the graph
from IPython.display import Image, display
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

# Run the graph
inputs = {"messages": [("user", "what is the weather in bangkok, Thailand?")]}
print_stream(graph.stream(inputs, stream_mode="values"))

