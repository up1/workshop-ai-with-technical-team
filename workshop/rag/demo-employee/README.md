# Workshop with search employee in your company
1. Database to store employee data in Relational database
   * [SQLite](https://www.sqlite.org/)
2. Embedding data for search and store in Vector database
   * [OpenAI Embedding](https://platform.openai.com/docs/guides/embeddings)
   * [ChromaDB](https://www.trychroma.com/)
4. Retrieve data from Vector database
5. Create prompt + data and send to LLM Provider
   * [OpenAI model](https://platform.openai.com/docs/guides/embeddings)


## Step 0 :: Initial project with Python
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
```

## Step 1 :: Install dependencies
```
$pip install -r requirements.txt
```

## Step 2 :: Initial data of employee in SQLite database
```
$python step_1_initial_data.py
```

Save all data in file `test_db.db`

## Step 3 :: Embedding data for search and save in to Vector Database
* OpenAI embedding model
* ChromaDB

Try to denomalize data into searchable format
```
Employee name : John Doe
Job title : Software Engineer
Department : IT
Office location : Chicago Office
```

Run
```
$export OPENAI_API_KEY=<your key>
$python step_2_save_to_vector_db.py
```

SAve all data in folder `employee_db/`

## Step 4 :: Retrieval data from Vector database and send request to LLM provider
* Langchain
* OpenAI

Run
```
$export OPENAI_API_KEY=<your key>
$python step_3_search_and_prompt.py
```

## Step 5 :: Evaluate actiual result with expected result
* [Confident AI QuickStart](https://docs.confident-ai.com/confident-ai/confident-ai-introduction)
  * Great LLM Evaluation==Quality of Dataset×Quality of Metrics
* [DeepEval](https://docs.confident-ai.com/)
  * Correctness metric

Run
```
$deepeval test run test_correctness.py
```


