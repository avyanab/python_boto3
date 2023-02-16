import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("wk14-py-ab")

response = bucket.create(
    ACL='public-read'
)

print(response)