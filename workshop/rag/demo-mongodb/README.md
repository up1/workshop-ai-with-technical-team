# Demo RAG with MongoDB
1. Create data exmample and save to CSV file
  * Employees
2. Create Embedding data for Vector search
  * Store in MongoDB
  * Search data (vector search) from MongoDB
3. Query data with LLM provider
  * OpenAI API
  * Prompt compression
4. Working with [Langchain](https://www.langchain.com/) library

## Steps to run this workshop
* Python
* OpenAI APIs

### 0. Setup environment to run python
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
```

### 1. Install libraries
```
$pip install -r requirements.txt
```

### 2. Initial data for testing
* Employee data
* File `step_1_initial_data.py`

Run
```
$python step_1_initial_data.py
```

Check employee data in file `employees.csv`

### 3. Embedding data for vector search
* File `step_2_embedding.py`

Run
```
$export OPENAI_API_KEY=<your key>
$python step_2_embedding.py
```

### 4. Save data into MongoDB
* File `step_3_save_to_mongodb.py`

Start MongoDB with Docker
```
$docker compose up -d
$docker compose ps
NAME                   IMAGE     COMMAND                  SERVICE   CREATED         STATUS         PORTS
demo-mongodb-mongo-1   mongo:8   "docker-entrypoint.s…"   mongo     3 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp
```

Run
```
$export MONGO_URI=mongodb://localhost:27017/?directConnection=true
$python step_3_save_to_mongodb.py
```

Check data in MongoDB
* database name = demo_employees

### 5. RAG with MongoDB
* File `step_4_rag_with_mongodb.py`

Run
```
$python step_4_rag_with_mongodb.py
```


