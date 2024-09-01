# Workshop :: RAG (Retrieval-Augmented Generation)
* Prompt template
* Prompt Injection

## Requirements
* Python 3+
* OpenAI API Key

## Initial
```
$pip install -r requirements.txt
```

## Run with OpenAPI's Key
```
$export OPENAI_API_KEY=<your key>
$python rag-openai.py
```

## Run with Ollama
* [Ollama python](https://github.com/ollama/ollama-python)
* [Langchain Ollama](https://python.langchain.com/v0.2/docs/integrations/llms/ollama/)
```
$python rag-ollama.py
```