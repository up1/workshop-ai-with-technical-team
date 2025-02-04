# AI Agent with [Aider](https://aider.chat/)


## [Install Aider](https://aider.chat/docs/install/install.html)
```
$python -m venv ./demo/venv
$source ./demo/venv/bin/activate
$python -m pip install aider-chat
```

## Config LLM Provider :: API KEY
```
// Anthropic API
$export ANTHROPIC_API_KEY=your-api-key
$aider

// OPENAI API
$export OPENAI_API_KEY=your-api-key
$aider

// Ollama :: https://aider.chat/docs/llms/ollama.html
$export OLLAMA_API_BASE=http://127.0.0.1:11434
$aider --model ollama/llama3.1

// Start Aider in browser
$aider --browser
```

## Start project with Aider with [OpenAI](https://aider.chat/docs/llms/openai.html)


Create file `index.js`
```
$aider index.js
```

## Create GET /products/:id
```
create a rest api with nodejs and express library
GET /products/:id that return

GET /products/1
Success case with response code = 200
{
"id": 1,
"name": "product name",
"price": 100.50
}
```

## Add case 404
```
Improve code to add case 404 for product not found

GET /products/2
Success case with response code = 404
{
"message": "Product id = 2 not found in system"
}
```

## Add case 500
```
Improve code to add case 500 for database or internal error

GET /products/3
Success case with response code = 500
{
"message": "System error"
}
```

## More prompts
* Refactor to split code into 2 files, index.js and app.js
* Add test case with supertest for app.js in folder `__tests__`
* Refactor to move GET /products/:id to file product.route.js 
* Review code
  * /ask review
  * /ask review `app.js`
* Run test
  * /test npm run test
* Add documents
  *  Generate sequence diagram of Oauth 2 in mermaid diagram and list of step-by-st
ep of process
  * Create OpenAPI Doc or swagger 3 , from rest api with nodejs and express libra
ry : GET /products/:id that return { 
"id": 1, "name": "product name", "price": 100.50}

## Initial project
```
$npm init -y
$npm install -S express
$npm install -D jest supertest
```

## Run test
Edit file `package.json`
```
"scripts": {
    "test": "jest"
  }
```

Run
```
$npm test
```
