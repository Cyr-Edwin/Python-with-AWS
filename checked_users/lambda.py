# import modules
import boto3
import json
from datetime import datetime

# services
sns = boto3.client('sns')
ami = boto3.client('iam')

# create Lambda function
def lambda_handler(event , context):

    try:
         
        # list all AMI users
        ami_users = ami.list_users()['Users'][0]['UserName']

        # iterate through user list
        for username in ami_users:
            #print(user)
            # check user password status
            password = ami.get_login_profile(UserName=username)
            if  'LoginProfile' not in password:
                send_email( username , "Missing Loging")
            
            # check MFA status
            mfa = ami.list_mfa_devices(UserName=username)
            if not mfa['MFADevices']:
                 send_email( username , "MAF not Enable")

            # check tags status
            tags =ami.list_user_tags(UserName=username)
            if not tags['Tags']:
                send_email( username , "Not tagged  ")




    except Exception as e:
        #print(f"Error: {e}")
        send_email('Lambda Fuction' , e)

# send email
        def send_email(name , message):
            topic_arn ="arn:aws:sns:us-east-1:511516667116:lambda"
            body = f'Time: {datetime.now()}\nUsername: {name}\nIssue:{message}'
            subject = f'AWS IAM USER Check -{name} - {message}'
            response = sns.publish(
    TopicArn=topic_arn,
    Message=body,
    Subject=subject 

      )

            '''# create subject
            subject = f'AWS IAM USER Check -{name} - {message}'
            # create body
            body = f'Time: {datetime.now()}\nUsername: {name}\nIssue:{message}'
            client = ses.send_email(
                Source = 'cyredwin1@gmail.com',
                Destination = {
                    'ToAddresses':['cyredwin1@gmail.com']
                },
                Message = {
                    'Subject': {'Data': subject},
                    'Body': {'Text':{'Data': body}}
                }
            )'''