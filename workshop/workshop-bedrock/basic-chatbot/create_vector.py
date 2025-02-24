import boto3
from langchain_aws import BedrockEmbeddings, ChatBedrock
from langchain_community.vectorstores.faiss import FAISS
from config import aws_access_key, aws_region_name, aws_secret_key

def create_client():
    bedrock = boto3.client(service_name='bedrock-runtime',
                        region_name=aws_region_name,
                        aws_access_key_id =aws_access_key,
                        aws_secret_access_key =aws_secret_key
                        )
    return bedrock

def create_llm(bedrock_client):
    llm = ChatBedrock(model_id='anthropic.claude-3-5-sonnet-20241022-v2:0', 
                  client=bedrock_client,
                  streaming=True,
                  model_kwargs={'temperature':0, 'top_p':0.9})
    return llm

def create_vector_store(docs):
    # Set up bedrock client
    bedrock = create_client()
    bedrock_embeddings = BedrockEmbeddings(model_id='amazon.titan-embed-text-v2:0', client=bedrock)

    # create and save the vector store
    vector_store = FAISS.from_documents(docs, bedrock_embeddings)
    vector_store.save_local("faiss_index")
    
    return None