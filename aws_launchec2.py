import boto3

ec2_resource=boto3.resource('ec2')

response = ec2_resource.create_instances(ImageId='ami-0dfcb1ef8550277af',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    SubnetId='string', # Enter your subnet ID
    TagSpecifications=[
        {'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name', 
                    'Value': 'string', # This will be the name of the instance
                },
                    {
                        'Key': 'string', # This is an additional tag for the instance
                        'Value': 'String',
                    }
                ]
            }
        ]
    )
print(response)