import boto3

client=boto3.client("ec2")

# will describe all vpcs 
response = client.describe_vpcs()
print(response)