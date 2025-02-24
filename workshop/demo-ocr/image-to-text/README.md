# Workshop with Image to Text with OpenAI


## Solution 1 :: Using OCR (Optical Character Recognition)
* pytesseract
* easyocr

```
$python solution_1.py
```

## Solution 2 :: Using LLM Model
* Convert image to base64
* Send data to OpenAI
  * data:image/png;base64
* LLM providers
  * OpenAI
  * Gemini

```
$export OPENAI_API_KEY=<your key>
$python solution_2.py
```