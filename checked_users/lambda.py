# import modules
import boto3
import json
from datetime import datetime

# services
ses = boto3.client('ses')
ami = boto3.client('ami')

# create Lambda function
def lambda_handler(event , context):

    try:
         
        # list all AMI users
        ami_users = ami.list_users()['Users']['UserName']

        # iterate through user list
        for user in ami_users:
            print(user)

    except:
        pass