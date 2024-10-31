# Demo :: Fine-tuning with OpenAI

## 1. Install libraries
```
$pip install -r requirements.txt
```

## 2. Sample with `chat.py`
```
$python chat.py
```


## 3. Fine-tuning with GPT-4o mini model
* Model = gpt-4o-mini

### Steps for tuning
1. Provide dataset
2. Pre-processing dataset
3. Split the dataset into training and validation sets
4. Save both the training and validation sets in JSONL format
5. Upload dataset to OpenAI
   * Upload both the training and validation dataset for fine-tuning
6. Start fine-tuning job


### Reference websites
* [Fine-tuning GPT-4o Mini: A Step-by-Step Guide](https://www.datacamp.com/tutorial/fine-tuning-gpt-4o-mini)
* [OpenAI fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)