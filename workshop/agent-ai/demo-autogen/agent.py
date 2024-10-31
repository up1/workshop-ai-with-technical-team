import autogen
from autogen.coding import LocalCommandLineCodeExecutor

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={"tags": ["gpt-4o"]},  # comment out to get all
)

# Create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "cache_seed": 41,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

# Create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER", # NEVER, AUTO, or PROMPT
    max_consecutive_auto_reply=10, # maximum number of auto-replies
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        # the executor to run the generated code into `coding/` directory
        # Reference :: https://microsoft.github.io/autogen/0.2/docs/tutorial/code-executors/
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
    },
)

# The assistant receives a message from the user_proxy, which contains the task description
chat_res = user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Compare the year-to-date gain for META and TESLA.""",
    summary_method="reflection_with_llm",
)

print("Chat history:", chat_res.chat_history)
print("Summary:", chat_res.summary)
print("Cost info:", chat_res.cost)

# Generate code to compare the year-to-date gain for META and TESLA
user_proxy.send(
    recipient=assistant,
    message="""Plot a chart of their stock price change YTD. 
    Save the data to stock_price_ytd.csv, 
    and save the plot to stock_price_ytd.png.""",
)