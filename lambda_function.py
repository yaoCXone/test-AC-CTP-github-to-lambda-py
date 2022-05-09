import pandas as pd
import json
import urllib.parse
import boto3

print('Loading function')

def lambda_handler(event, context):
    s3_to_lambda(event, context)

def main():   
    d={'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def s3_to_lambda(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print('bucket: '+bucket)
    print('key: '+key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

if __name__ == "__main__":
    main()

