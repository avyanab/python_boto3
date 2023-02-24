import boto3

ec2 = boto3.resource('ec2')
ids = ['str']

response = ec2.instances.filter(InstanceIds = ids).terminate()
print(response)
