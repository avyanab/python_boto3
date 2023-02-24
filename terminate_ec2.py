import boto3

ec2 = boto3.resource('ec2')
ids = ['i-0f46e6813f1079ec7','i-008664e94b628889e', 'i-05c42eec3cb49a529']

response = ec2.instances.filter(InstanceIds = ids).terminate()
print(response)
