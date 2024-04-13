import boto3
import json


class TextPrompt(object):

    @staticmethod
    def generate(prompt: str):
        bedrock = boto3.client('bedrock-runtime', region_name="us-east-1")
        payload = {
            "prompt": prompt,
            "max_gen_len": 2048,
            "temperature": 0.5,
            "top_p": 0.9
            }
        

        body = json.dumps(payload)
        model_id = "meta.llama2-13b-chat-v1"
        response = bedrock.invoke_model(
            body=body,
            modelId = model_id,
            accept="application/json",
            contentType="application/json",
        )
        
        response_body = json.loads(response.get("body").read())


        response_text = response_body["generation"]

        return response_text