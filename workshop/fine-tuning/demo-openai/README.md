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
* Model = gpt-4o

### Steps for tuning
1. Provide dataset
2. Pre-processing dataset
3. Split the dataset into training and validation sets
4. Save both the training and validation sets in JSONL format
5. Upload dataset to OpenAI
   * Upload both the training and validation dataset for fine-tuning
6. Start fine-tuning job

### 3.1 Prepare dataset
* training-dataset.jsonl
```
{"messages": [{"role": "system", "content": "You are teaching assistant for Machine Learning. You should help to user to answer on his question."}, {"role": "user", "content": "What is machine learning?"}, {"role": "assistant", "content": "'Tis but the art of teaching machines to think, to learn from data most fine, and decisions to link."}]}

{"messages": [{"role": "system", "content": "You are teaching assistant for Machine Learning. You should help to user to answer on his question."}, {"role": "user", "content": "How doth neural networks work?"}, {"role": "assistant", "content": "They're like the brains of yon digital beast, with layers many, and nodes that cease."}]}
```

## 3.2 Upload training data file to OpenAI
```
$python 1_upload.py           

FileObject(id='file-Wn1lH03HRCN3nNvWtITYXItS', bytes=680, created_at=1730374381, filename='training-dataset.jsonl', object='file', purpose='fine-tune', status='processed', status_details=None)
```

Check file in OpenAI -> [Storage](https://platform.openai.com/storage)

## 3.2 Create a fine-tuned model with training data file from Step 3.2
```
$python 2_create_model.py

FineTuningJob(id='ftjob-NTTihP9RJaqluLAaWKld7wuW', created_at=1730374764, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(n_epochs='auto', batch_size='auto', learning_rate_multiplier='auto'), model='gpt-4o-2024-08-06', object='fine_tuning.job', organization_id='xxx', result_files=[], seed=1477410863, status='validating_files', trained_tokens=None, training_file='file-Wn1lH03HRCN3nNvWtITYXItS', validation_file=None, estimated_finish=None, integrations=[], user_provided_suffix=None)
```

Check result of fine-tuning in [OpenAI Fine-tuning](https://platform.openai.com/finetune)

## 3.3 Use your model
```
$python 3_use_fine_tune_model.py
```


### Reference websites
* [OpenAI fine-tuning UI](https://platform.openai.com/finetune)
* [OpenAI fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)
* [Fine-Tuning OpenAI's GPT-4: A Step-by-Step Guide](https://www.datacamp.com/tutorial/fine-tuning-openais-gpt-4-step-by-step-guide)
* [Fine-tuning GPT-4o Mini: A Step-by-Step Guide](https://www.datacamp.com/tutorial/fine-tuning-gpt-4o-mini)