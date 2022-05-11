import src.panads_sample as ps
import src.lambda_function as lf
import samples.event_samples as evts
import src.crt_processor as crt
import json

def main():
	body = crt.read_file_binary('C:\\temp\\sample-event')
	#body = crt.read_file_binary('C:\\temp\\1092107.cjs')
	content = lf.load_json_from_binary(body)
	print(content)

def lambda_handler_test(event, context):
    lf.s3_to_lambda(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda function!')
    }


if __name__ == "__main__":
	main()