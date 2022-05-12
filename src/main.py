import panads_sample as ps
import s3_ctr as ctr
#from ..//sample//event_samples import event_1 as evt1
import json
from pathlib import Path
import lambda_function as lf

def main():	
	body = read_file_binary('C:\\temp\\sample-event')
	#body = read_file_binary('C:\\temp\\1092107.cjs')
	content = ctr.load_json_from_binary(body)
	print(content)

def lambda_handler_test(event, context):
    #lf.s3_to_lambda(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda function!')
    }


def read_file_binary(file_path):
	return Path(file_path).read_bytes() # Python 3.5+

if __name__ == "__main__":
	import sys
	main()