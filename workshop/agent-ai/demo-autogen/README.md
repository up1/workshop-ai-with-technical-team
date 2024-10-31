# Demo with Agent AI
* [Microsoft AutoGen](https://microsoft.github.io/autogen)
   * AssistantAgent
   * UserProxyAgent
* Try to write code and execute code !!
* Working with OpenAI API

## Step 0 :: Initial
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
```

## Step 1 :: Install dependencies
* [Install AutoGen](https://microsoft.github.io/autogen/0.2/docs/installation/)
* AutoGen requires Python version >= 3.8, < 3.13
```
$pip install -r requirements.txt -U
```

## Step 2 :: Run agent

2.1 Create file `OAI_CONFIG_LIST`
```
[
    {
        "model": "gpt-4o",
        "api_key": "***",
        "tags": ["gpt-4o"]
    },
    {
        "model": "gpt-3.5-turbo",
        "api_key": "***",
        "tags": ["gpt-3.5"]
    }
]
```

2.2 Run Agent
```
$python agent.py
```


### Fix errors
```
$brew install libomp
```

### Reference websites
* [Task Solving with Code Generation, Execution and Debugging](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_auto_feedback_from_code_execution)