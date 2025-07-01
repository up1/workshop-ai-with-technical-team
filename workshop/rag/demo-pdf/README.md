# Demo with PDF file
* Read data from PDF
* Create embedding and save to vector database
* Retriever data from vector database
* Senf prompt to OpenAI


## Install dependencies
```
$pip install -r requirements.txt
```

## Run with OpenAPI's Key
```
$export OPENAI_API_KEY=<your key>

// Store data in Vectoe DB
$python step_01_store.py

// Search or retrive data
$python step_02_retrieve.py

// Chat with AI
$python step_03_chat.py
```