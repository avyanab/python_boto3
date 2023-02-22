# Code for my lambda function to send a message with current date and time in UTC to Amazon SQS 
import json
import boto3

from datetime import datetime, timezone


def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    local_time = datetime.now(timezone.utc)
    queue = sqs.Queue(url='string')
    
    response = queue.send_message(MessageBody=str(local_time))
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }