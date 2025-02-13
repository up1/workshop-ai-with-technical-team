# Demo :: Agentic AI with RAG
* [Agno](https://github.com/agno-agi/agno) is a lightweight framework for building multi-modal Agents
* OpenAI
* [LanceDB](https://lancedb.com/)
  * Vector database :: open source database for AI


## 1. Install dependencies
```
$pip install -r requirements.txt
```

## 2. Run and interact in web browser
```
$export OPENAI_API_KEY=<your key>
$python demo_agent.py

INFO     Creating collection                                                           
INFO     Loading knowledge base                                                        
INFO     Reading: https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf          
INFO     Added 0 documents to knowledge base                                           
INFO     Starting playground on http://localhost:7777                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Agent Playground ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                             ┃
┃                                                                             ┃
┃  Playground URL: https://app.agno.com/playground?endpoint=localhost%3A7777  ┃
┃                                                                             ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```