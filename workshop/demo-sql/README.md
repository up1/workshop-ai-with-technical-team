# Demo :: Text to SQL
* Create database ans tables
* Insert sample data
* Read schema and send to LLM provider
* Question and Answer with LLM provider
* LLM Providers
  *  Anthropic
  *  OpenAI
  *  Ollama 

## Steps to run
```
$pip install -r requirements.txt

$export ANTHROPIC_API_KEY=<your key>
$python demo-sql.py
```

If you got error, please remove file `test_db.db`

## More
* Security in edge cases
  * Delete data in table
  * Drop table


### References
* [Anthropic example](https://github.com/anthropics/anthropic-cookbook/tree/main/skills/text_to_sql)
* [Ollama:OpenAI compatibility](https://ollama.com/blog/openai-compatibility)
