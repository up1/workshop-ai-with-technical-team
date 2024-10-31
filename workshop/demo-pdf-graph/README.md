# Demo :: Read data from PDF file and generate chart from data
* [Anthropic API](https://docs.anthropic.com/en/docs/about-claude/models)
  * Model=claude-3-haiku-20240307
  * Model=claude-3-opus-20240229

## Step 0 :: Initial
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
```

## Step 1 :: Install dependencies
```
$pip install -r requirements.txt
```

## Step 2 :: Download PDF files and save to image files
* Save PDF files into folder `images/`
```
$python step_1_download_data.py
```

## Step 3 :: Extract data from PDF
* Save result to file `extracted_info.txt`
```
$python step_2_extract_data_from_pdf.py
```

## Step 4 :: Working with model=`claude-3-opus-20240229`
```
$python step_3_question_with_opus.py
```
