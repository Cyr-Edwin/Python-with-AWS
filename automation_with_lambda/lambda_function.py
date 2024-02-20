# import module
import boto3

ec2 = boto3.client("ec2")

def lambda_handler(event , content):
    # get userName from user
    user_name = event['detail']['userIdentity']['userName']

    # get instance ID
    instance_id = event['detail']['responseElements']['instancesSet'][0]['instanceId']
    
    # create tag on EC2 instance 
    ec2.create_tags(
        Resources=[
        instance_id,
    ],
    Tags=[
        {
            'Key': 'Owner',
            'Value': user_name
        },
    ])
    return