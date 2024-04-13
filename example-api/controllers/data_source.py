import boto3
import json


class Data_Source(object):

    @staticmethod
    def list():
        
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        buckets = [{'Name': bucket['Name'], 'CreationDate': bucket['CreationDate'].isoformat()} for bucket in response['Buckets']]
        return json.dumps(buckets, indent=4)
        