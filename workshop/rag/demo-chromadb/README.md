# RAG with [ChromaDB](https://www.trychroma.com/)


## 1. Install dependencies
```
$pip install -r requirements.txt
```

## 2. Load data and save into vector database
```
$set USER_AGENT=123
$python step_1.py
```

Create a new files amd folders in folder `demo.db/`

## 3. Retriever and generate response from LLM
```
$python step_2.py
```