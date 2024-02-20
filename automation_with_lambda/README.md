# Write a Lambda function on AWS that adds Tag to the EC2 instance which has been created by a user

<h6> Services used<h6>

* EC2

* Lambda function

* IAM

* EventBridge

* CloudTrail

<h6>Implimentation<h6>

<h1>Lambda Function<h1>

* Create Lambda Function on AWS:
   
. Runtime : Python.xx

. Add permissions to Lambda to create tags on EC2 instance

. Create a simple test to have log groups (Clicked: **Monitor** and **View CloudWatch logs**)

<h1>CloudTrail<h1>

* Create a Trail on AWS:

. Create a S3 bucket to save logs

. CloudWatch Logs : Enabled

. Create an IAM Role : AWS CloudTrail assumes this role to send CloudTrail events to your CloudWatch Logs log group

<h1>EventBridge<h1>

* Create Rule on AWS:

. Rule type : Rule with an event patter

. Event source : All events

. Creation method : Use pattern form

. Event pattern : Event source(AWS Services) , AWS service (EC2) , Event type (AWS API Call via CloudTrail)

. Event Type Specification 1 : Specific operation(s)(RunInstances)

. Event pattern code block:

``
{
  "source": ["aws.ec2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ec2.amazonaws.com"],
    "eventName": ["RunInstances"]
  }
}
`` 

. Target types : AWS service

. Select a target : Lambda Function 

. Function : choose the function you created