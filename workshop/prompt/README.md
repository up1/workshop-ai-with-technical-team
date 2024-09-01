# Workshop with Prompt
* Static prompt
* Prompt template
* Prompt pipeline
* Prompt chain

## Software requirement
* Pythom 3+
* OpenAI's api key

## Initial project
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
$pip install -r requirements.txt
$EXPORT OPENAI_API_KEY=<your key>
```

## Contextually engineered Prompt
* Instruction
* Context
* Question

## 1. Static prompt
```
$python 01-static.py
```

## 2. Improve answer
* Hallucination problem
```
$python 02-static-improve.py
```

## 3. Improve answer with add more context
* Hallucination problem
```
$python 03-static-improve-context.py
```

## 4. Read context data from text file
```
$python 04-read-file.py
```