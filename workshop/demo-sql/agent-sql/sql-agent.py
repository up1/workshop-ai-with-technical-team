from langchain_community.utilities import SQLDatabase
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.chains import create_sql_query_chain 
import os
from dotenv import load_dotenv
load_dotenv()

# define the database we want to use for our test
db = SQLDatabase.from_uri('sqlite:///../test_db.db')

# choose llm model, in this case the default OpenAI model
llm = OpenAI(
            temperature=0, 
            verbose=True,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            )

# Setup chain
chain = create_sql_query_chain(llm, db)
# Ask a question
question = "What are the names and salaries of employees in the Engineering department?"
response = chain.invoke({"question": "How many employees are there"})
print(response)