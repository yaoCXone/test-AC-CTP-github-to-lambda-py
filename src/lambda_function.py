import json
from s3_ctr import s3_json_object as S3JsonObject
import urllib.parse

print('Loading function')

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
    print("Received notification of bucket:(" + bucket + ") key:(" + key +") content change.")
    try:       
        json_obj = S3JsonObject(bucket, key)
        json_content = json_obj.read_json_contects()

        if(json_content is None):
            print("Invalid json content from object in bucket:(" + bucket + ") key:(" +key+")")
        else:
            print(body)
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e



