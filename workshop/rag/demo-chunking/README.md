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

