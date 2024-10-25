# Workshop RAG Locally
* LLM server: Ollama local server 
* LLM model: LLama 3 
* Embedding model: all-MiniLM-L6-v2
  * HuggingFaceEmbeddings
* Vector database: SQLiteVSS (sqlite3)
* Framework: LangChain

## Step 1 :: Install
```
$pip install -r requirements.txt
```

## Step 2 :: Run
* [LangSmith](https://docs.smith.langchain.com/)
```
$export LANGCHAIN_TRACING_V2=true
$export LANGCHAIN_API_KEY=<your-api-key>
$export TOKENIZERS_PARALLELISM=false

$python demo.py
```
