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

## 5. Retriever and generate response from LLM
```
$python step_4.py
```

## Improvement :: 6. Re-ranking with FlashRank reranker
* https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/

Before
```
$python step_5.py
```

After with 
```
$python step_6.py
```

## Improvement :: 7. Re-ranking with Cohere
* https://docs.cohere.com/v2/docs/rerank-on-langchain
* https://dashboard.cohere.com/api-keys

```
$export COHERE_API_KEY=<api key>
$python step_7.py
```

## 8. Run with Cohere
```
$python step_8.py
```