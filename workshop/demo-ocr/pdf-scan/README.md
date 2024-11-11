# Demo :: Read data from PDF file
* Scan image to PDF (real problem)

## Steps of thinking
1. Read pdf file
2. Convert from pdf to image (page-by-page)
3. Read text from image (OCR)
   * Thai and English
4. Improve quality with LLM provider


### 0. Install libraries
File `requirements.txt`
```
pymupdf
easyocr
```

Install
```
$pip install -r requirements.txt
```

### 1. Convert from pdf to image (page-by-page)
```
$python 1-pdf-to-image.py 
```
Results :: Image file per page
* image_1.png
* image_2.png
* image_3.png
* image_4.png

### 2. Read text from image (OCR)
```
$python 2-image-to-text.py
```

Results :: `page_1.txt`

### 3. Improve quality with LLM provider
* OpenAI API
```
$export OPENAI_API_KEY=<your api key>
$python 3-fix-text-by-openai.py 
```

Results :: `page_1_fixed.txt`

### 4. Improve quality with LLM provider
* Ollama + llama3.2:3b
```
$python 4-fix-text-by-ollama.py
```

Results :: `page_1_fixed_ollama.txt`

### 5. RAG
* Embedding data and save into Vector database
  * OpenAI's embedding
  * Vector database = [FAISS](https://python.langchain.com/docs/integrations/vectorstores/faiss/)
* Search relevent data
* Send to LLM provider
  * OpenAI

### 5.1 Create embedding and save into file
* [Chunking](https://python.langchain.com/docs/how_to/character_text_splitter/)
* Embedding
```
$python 5-rag-embedding.py
```
Results :: Create folder `data.faiss`

### 5.2 relevent data and send to OpenAI API
```
$python 6-rag-search.py
```

### 5.3 Compression context
```
$python 7-rag-search-compression.py
```

### Reference websites
* [Python OCR libraries for converting PDFs into editable text](https://ploomber.io/blog/pdf-ocr/)
* [FullStackRetrieval.com](https://community.fullstackretrieval.com/)