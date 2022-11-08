import os
import io
import boto3
import json
import csv

"""
Ref: API impl: https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/
IAM Policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sagemaker:InvokeEndpoint",
            "Resource": "*"
        }
    ]
}
"""
# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("[INFO] LAMBDA PROXY Received event: " + json.dumps(event, indent=2))
    
    print("[INFO] ENDPOINT_NAME: ", ENDPOINT_NAME)
    data = json.loads(json.dumps(event))
    payload = data['image_name']
    # payload = data['data']
    print("[INFO] PAYLOAD :", payload)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Accept='application/json',
                                       Body=payload)
    print("[INFO] RESPONSE :", response)
    
    resp_body = response['Body'].read().decode('utf-8').strip()
    print("[INFO] resp_body :", resp_body)
    
    result = '{"predict": "'+ resp_body +'"}'

    result = json.loads(result)
    print("[INFO] result :", result)
    
    return result