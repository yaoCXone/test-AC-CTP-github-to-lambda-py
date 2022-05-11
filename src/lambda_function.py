import json
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
    print('bucket: '+bucket)
    print('key: '+key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print("Received notification of bucket:(" + bucket + ") key:(" +key+") content change.")
        body = read_s3_contents(response)
        print(body)
        try:
            records_json = json.loads(body)
            print(records_json)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Invalid JSON from response body')
        #return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


def read_s3_contents(response):
    # open the file object and read it into the variable filedata. 
    filedata = response['Body'].read()

    # file data will be a binary stream.  We have to decode it 
    return filedata.decode('utf-8') 


