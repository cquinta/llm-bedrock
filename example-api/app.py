import json
import os
import sys
import boto3

# Embeddings

from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import bedrock

def get_vector_store():
    # Cria um cliente para o serviço OpenSearch
    vector_store=BedrockEmbeddings(model_id='anthropic.claude-v2:1', client=bedrock)
    return vector_store

def get_cloud_llm():
    # Cria um cliente para o serviço OpenSearch
    llm=Bedrock(model_id='anthropic.claude-v2:1', client=bedrock,
                model_kwargs={'maxtokens':512})
    return llm

def get_llama2_llm():
    # Cria um cliente para o serviço OpenSearch
    llm=Bedrock(model_id='meta.llama2-70b-chat-v1', client=bedrock,
                model_kwargs={'maxtokens':512})
    return llm


