import matplotlib, pandas, shapely, json

def lambda_handler(event, context):
    response = "Hello World. Docker - Github Actions - AWS ECR - CICD Pipeline"
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
