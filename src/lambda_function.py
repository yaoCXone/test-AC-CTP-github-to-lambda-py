import json
from json.decoder import JSONDecodeError
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    s3_to_lambda(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda function!')
    }

def s3_to_lambda(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8') 
    print("Received notification of bucket:(" + bucket + ") key:(" +key+") content change.")
    try:        
        body = read_s3_contents(bucket, key)
        if(body is None):
            print("Invalid json content from object in bucket:(" + bucket + ") key:(" +key+")")
        else:
            print(body)
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def read_s3_contents(bucket, key):
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        body = read_s3_contents(response)        
        return load_json_from_binary(body)

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def load_json_from_binary(binary_data):
    try:
        return json.loads(binary_data)
    except JSONDecodeError as e:
        print(e)
        print("Error in loading json binary data")
    except ValueError as ve:
        print(ve) 
        print('Invalid JSON value in string')
    except TypeError as te:
        print(te) 


