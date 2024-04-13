
import json
import os
import boto3 # type: ignore
import pprint
from utility import create_bedrock_execution_role, create_oss_policy_attach_bedrock_execution_role, create_policies_in_oss
import random
from retrying import retry # type: ignore
import time

class Vector_Store(object):
    def create(name: str):
        suffix = random.randrange(1000,2000)
        sts_client = boto3.client('sts')
        boto3_session = boto3.session.Session()
        region_name = boto3_session.region_name
        

# Create a S3 bucket
        s3_client = boto3.client('s3')
        account_id = sts_client.get_caller_identity()["Account"]
        s3_suffix = f"{region_name}-{account_id}"
        bucket_name = f'bedrock-kb-{name}-{s3_suffix}' # replace it with your bucket name.
        pp = pprint.PrettyPrinter(indent=2)
        s3bucket = s3_client.create_bucket(Bucket=bucket_name)

# Create Vector Store
        vector_store_name = f'bedrock-sample-rag-{name}-{suffix}'
        index_name = f"bedrock-sample-rag-index-{name}-{suffix}"
        aoss_client = boto3_session.client('opensearchserverless')
        bedrock_kb_execution_role = create_bedrock_execution_role(bucket_name=bucket_name)
        bedrock_kb_execution_role_arn = bedrock_kb_execution_role['Role']['Arn']

#Create policies in OSS
        encryption_policy, network_policy, access_policy = create_policies_in_oss(vector_store_name=vector_store_name,
                       aoss_client=aoss_client,
                       bedrock_kb_execution_role_arn=bedrock_kb_execution_role_arn)
        
        collection = aoss_client.create_collection(name=vector_store_name,type='VECTORSEARCH')
        collection_id = collection['createCollectionDetail']['id']
        host = collection_id + '.' + 'us-east-1' + '.aoss.amazonaws.com'
        return(host)
        
        