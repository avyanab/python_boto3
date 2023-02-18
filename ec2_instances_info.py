import boto3

ec2 = boto3.resource('ec2')
    
for instance in ec2.instances.all():
    print(
         "Id: {0}\nTag: {1}\nType: {2}\nAMI: {3}\nState: {4}\n".format(
         instance.id, instance.tags, instance.instance_type, instance.image.id, instance.state
         )
     )