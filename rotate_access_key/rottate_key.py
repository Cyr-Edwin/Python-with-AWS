# import modules
import boto3
from botocore.exceptions import ClientError
from datetime import date

# create a new IAM resource
iam = boto3.client("iam")

# send emails
def send_email(RECIPIENT_LIST , SENDER , SUBJECT , BODY_TEXT , YOUR_REGION):

    # create a new SES resource and specify AWS region
    ses = boto3.client("ses" ,region_name = YOUR_REGION )
    
    CHARSET = "UTF-8"


    try:
        response = ses.send_email(

        source = SENDER,

        Destination={

        'ToAddresses': RECIPIENT_LIST,
    },

    Message={

        'Subject': {
            'Data': SUBJECT,
            'Charset': CHARSET
        },

        'Body': {
            
            'Text': {
                'Data': BODY_TEXT,
                'Charset': CHARSET
            },
        }
    },
    )
        
    except ClientError as e:

        print(e.response["Error"]["Message"])
    
    else:

        print(f"Email sent..."+"\n")

        print(f"Email ID",{response["MessageId"]})