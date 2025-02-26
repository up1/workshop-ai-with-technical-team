# Workshop Semi-structure
* PDF file(table and text)
* [Multi-retriever](https://github.com/langchain-ai/langchain/blob/master/cookbook/Semi_Structured_RAG.ipynb?ref=blog.langchain.dev)


## Step 1 :: Install software
* [tesseract](https://github.com/tesseract-ocr/tesseract) for Optical Character Recognition (OCR)
* [poppler](https://poppler.freedesktop.org/) for PDF rendering and processing

Install in MacOS
```
$brew install tesseract
$brew install poppler
```

## Step 2 :: Install libraries
```
$pip install -r requirements.txt
```

## Step 3 :: Read and extract tables from pdf file
* [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX/)
* [Unstructured.io](https://docs.unstructured.io/welcome)

```
$python step_1_load_data.py


yolox_l0.05.onnx: 100%|███████████████████████████████████| 217M/217M [00:33<00:00, 6.39MB/s]
config.json: 100%|██████████████████████████████████████| 1.47k/1.47k [00:00<00:00, 4.52MB/s]
model.safetensors:   0%|                                          | 0.00/115M [00:00<?, ?B/s]
model.safetensors: 100%|██████████████████████████████████| 115M/115M [00:17<00:00, 6.68MB/s]
model.safetensors: 100%|████████████████████████████████| 46.8M/46.8M [00:06<00:00, 6.75MB/s]

Number of tables in pdf:  2
```

## Step 4 :: Grouping data
* Table
* Text
 
```
$python step_2_load_and_grouping.py
```