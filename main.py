import src.panads_sample as ps
import src.lambda_function as lf
import samples.event_samples as evts
import json

def main():
	evt = evts.event_1()
	
	serialized = json.dumps(evt, sort_keys=True, indent=4)
	print(serialized)
	## lf.s3_to_lambda(evt, "context")
	## now we are gonna convert json to object
	deserialization=json.loads(serialized)
	print(deserialization)
	ps.print_sample_2x2()

def lambda_handler_test(event, context):
    lf.s3_to_lambda(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda function!')
    }


if __name__ == "__main__":
	main()