import boto3

sqs = boto3.resource('sqs') # Defining sqs as the service resource


queue = sqs.create_queue( # Create the queue. This returns an SQS.Queue instance
    QueueName='string', 
    Attributes={'DelaySeconds': '10'}
)

print(queue.url) # Will return new queue's URL 
print(queue.attributes.get('DelaySeconds')) # To access queue identifiers and attributes