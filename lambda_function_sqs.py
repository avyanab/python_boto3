# Code for my lambda function to send a message with current date and time in EST to Amazon SQS 
import json, boto3, dateutil

from datetime import datetime, timezone


def lambda_handler(event, context):
    sqs = boto3.resource('sqs') # Setting sqs as the resource
    local_time = datetime.now(dateutil.tz.gettz('US/Eastern')) # Obtain date and time in Eastern Standard Time
    time_msg = local_time.strftime('Hi! It is now %I:%M%p on %B %d, %Y.') # The local time will be formatted with a greeting
    queue = sqs.Queue(url='str') # Enter the URL of queue to work with
    
    queue.send_message(MessageBody=time_msg) # Will send a message to queue with a greeting, current time and date
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(local_time.strftime('%Y-%m-%d %H:%M'), default = str) # output will be current date, and 24hr time
    }