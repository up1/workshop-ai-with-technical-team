# Workshop :: Read data from image
* Skip from K-Bank
* OpenAI
* Python 3+

## Simple prompts
* [Starter prompt](https://github.com/up1/workshop-ai-with-technical-team/wiki/Workshop-::-Bank's-slip)

## Steps of workshop
* Install the required libraries.
* Import necessary modules.
* Load the image file.
* Use OCR to extract text from the image.
* Initialize OpenAI API with LangChain.
* Process the extracted text using OpenAI's API.
* Create backend with REST API
  * NodeJS
  * Express
* Create frontend
  * ReactJS
  * Axios


## Install
```
$pip install -r requirements.txt
```

## Read data from image file
```
$python 1-read-data-from-image.py
```

## Prompt to generate REST API to read data
* Libraries
  * express
  * @langchain/core
  * @langchain/openai
  * multer
  * tesseract.js

```
As a NodeJS developer, i want to generate code with NodeJS
POST /slip/upload
with multipart-form
* file upload

Response 200
{
    "bank": "KBank",
    "account_number": "XXX-X-X9323-x",
    "store": "AMZ_SD4330 UNION MAL",
    "company": "DEEMAPHARUAY CO., LTD.",
    "date": "202408202155006",
    "total_amount": "45.00 Baht"
}
```

Run and Testing ..
```
$export OPENAI_API_KEY=your api key
```

## Convert from Python to NodeJS
```
As a nodejs developer, i want to convert below code from Python to NodeJS
```

Run and Testing ..
```
$export OPENAI_API_KEY=your api key
```

## Prompt to generate UI of system
* [v0.dev](https://v0.dev/chat)
  * Generate UI to upload a file with reactjs and tailwind css
  * add button upload

Create React project
```
$npm create vite@latest
```

Add Tailwine css in index.html
```
<script src="https://cdn.tailwindcss.com"></script>
```

## Integate UI and Backend
* Send uploaded file to REST API with axios library POST /slip/upload
* nodejs, fix problem with CORS



