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