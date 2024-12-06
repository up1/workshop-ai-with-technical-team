# Demo with Chunking approach
* Libraries
  * [LangChain](https://python.langchain.com/docs/how_to/)

## Install libraries
```
$pip install -r requirments.txt
```

## Fixed-size chunking
* [CharacterTextSplitter](https://python.langchain.com/docs/how_to/character_text_splitter/)

```
$export OPENAI_API_KEY=your-api-key
$python python 1-fixed-size.py
```

## Structured-based chunking
* The aim of chunking is to keep meaningful data together
* [HTMLHeaderTextSplitter](https://python.langchain.com/docs/how_to/HTML_header_metadata_splitter/)

```
$python 2-structure-based.py
```

## Context-Enriched Chunking
* Working with LLM provider

### Steps
* Read data from website
* Summarize data from LLM provider
* Chunking
* Embedding and save to Vector database

```
$export OPENAI_API_KEY=your-api-key
$python 3-context-enriched.py
```

## Semantic Chunking
* RecursiveCharacterTextSplitter vs SemanticChunker

### Steps
1. Read data from PDF
2. Use [SemanticChunker](https://python.langchain.com/docs/how_to/semantic-chunker/) from langchain
3. Embedding with [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) from HuggingFace
4. LLM provider with Ollama


4.1 with RecursiveCharacterTextSplitter
```
$export TOKENIZERS_PARALLELISM=true
$python 5-native.py
```

4.2 with SemanticChunker
```
$export TOKENIZERS_PARALLELISM=true
$python 5-semantic.py
```




### Reference websites
* [Breaking It Down : Chunking for Better RAG](https://towardsdatascience.com/breaking-it-down-chunking-techniques-for-better-rag-3fd288bf25a0)
* [Semantic chunking](https://github.com/pavanbelagatti/Semantic-Chunking-RAG/blob/main/Semantic%20Chunking%20Tutorial.ipynb)
