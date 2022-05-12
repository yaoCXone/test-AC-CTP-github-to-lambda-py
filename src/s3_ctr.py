import json
from json.decoder import JSONDecodeError
import boto3

s3 = boto3.client('s3')

class s3_json_object:
	bucket=''
	key=''
	def __init__(self, bucket, key):
		self.bucket = bucket
		self.key = key

	def read_json_contects(self):
		return read_json_contents_from_s3_bucket(self.bucket, self.key)

def read_json_contents_from_s3_bucket(bucket, key):
    try:
        response = s3.get_object(Bucket = bucket, Key = key)
        print("CONTENT TYPE: " + response['ContentType'])
        binary_data = response['Body'].read()
        return load_json_from_binary(binary_data)

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




