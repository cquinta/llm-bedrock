import json
import os
import boto3  # type: ignore
import pprint
from utility import (
    create_bedrock_execution_role,
    create_oss_policy_attach_bedrock_execution_role,
    create_policies_in_oss,
)
import boto3
import random
import time
import json
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth


class Vector_Index(object):
    def create(store_name: str):
        
        credentials = boto3.Session().get_credentials()
        region_name = "us-east-1"
        service = "aoss"
        awsauth = auth = AWSV4SignerAuth(credentials, region_name, service)
        suffix = random.randrange(2000, 3000)

        index_name = f"bedrock-sample-index-{suffix}"
        body_json = {
            "settings": {
                "index.knn": "true",
                "number_of_shards": 1,
                "knn.algo_param.ef_search": 512,
                "number_of_replicas": 0,
            },
            "mappings": {
                "properties": {
                    "vector": {
                        "type": "knn_vector",
                        "dimension": 1536,
                        "method": {
                            "name": "hnsw",
                            "engine": "nmslib",
                            "space_type": "cosinesimil",
                            "parameters": {"ef_construction": 512, "m": 16},
                        },
                    },
                    "text": {"type": "text"},
                    "text-metadata": {"type": "text"},
                }
            },
        }
        # Build the OpenSearch client
        oss_client = OpenSearch(
            hosts=[
                {
                    "host": store_name,
                    "port": 443,
                }
            ],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            timeout=300,
        )
        return(oss_client.indices.create(index=index_name, body=json.dumps(body_json)))

    
