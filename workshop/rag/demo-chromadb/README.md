# RAG with [ChromaDB](https://www.trychroma.com/)
* Load document from web
* Split and chunking data into small pieces
* Embedding and save into Vector database
* Search ralevant data from Vector database
* Send query + relevant data/context to LLM provider

## 1. Install dependencies
```
$pip install -r requirements.txt
```

## 2. Load data from web
```
$export USER_AGENT=123
$python step_1.py
```

## 3. Chunking data with RecursiveCharacterTextSplitter
```
$python step_2.py
```

## 4. Embedding and save to Vector database
```
$python step_3.py
```

Create a new files amd folders in folder `demo.db/`

## 4. Retriever and generate response from LLM
```
$python step_4.py
```