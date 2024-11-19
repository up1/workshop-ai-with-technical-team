# LLM app with [Llama-index](https://docs.llamaindex.ai/)
* Read data from files
* Create Vector store
* Query data from Vector store
* Ask question + data in LLm Provider
  * OpenAI gpt-4o

## 0. Install library
```
$pip install -r requirements.txt
```

## 1. Basic of RAG
Run
```
$export OPENAI_API_KEY=<your key>
$python 01-basic.py
```

## 2. [Prompt template](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
Run
```
$export OPENAI_API_KEY=<your key>
$python 02-prompt-template.py
```