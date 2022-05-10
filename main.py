
import src.panads_sample as ps
import src.lambda_handler as lh

def main():
    ps.print_sample_2x2()

def lambda_handler(event, context):
    lh.s3_to_lambda(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda function!')
    }


if __name__ == "__main__":
	main()