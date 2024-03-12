# Write a Lambda function to notify a lead that an object was upload to a S3 bucket

## AWS Service Used

* Lambda Function

* Simple Storage Service (S3)

* Simple Notification Service (SNS)

* Identity Access Manager (IAM)

### Overview
this project enlights the use of Serverless Compute in a  Even-driven architecture. The Even-driven architecture is build with Python.

####  Architecture Diagram 



##### Implimentation

##### I Set up the Environment 

* Create AWS account

##### II Create a S3 bucket

* Create a bucket with a **Unique** name and keep everything as default or implimented based on your need bucket000001111111111

##### III Create a Policy

* The policy below allows to read from S3,  write and tag logs  into CloudWatch logs
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:DisassociateKmsKey",
                "logs:DeleteSubscriptionFilter",
                "logs:UntagLogGroup",
                "logs:DeleteLogGroup",
                "logs:DeleteLogStream",
                "logs:PutLogEvents",
                "logs:CreateExportTask",
                "logs:PutMetricFilter",
                "s3:GetObject",
                "logs:CreateLogStream",
                "logs:DeleteMetricFilter",
                "logs:TagLogGroup",
                "logs:DeleteRetentionPolicy",
                "logs:AssociateKmsKey",
                "logs:PutSubscriptionFilter",
                "logs:PutRetentionPolicy"
            ],
            "Resource": [
                "arn:aws:logs:*:511516667116:log-group:*:log-stream:*",
                "arn:aws:logs:*:511516667116:log-group:*",
                "arn:aws:s3:::bucket000001111111111/*"
    
            ]
        }
    ]
}
```

##### IV- Create Role

For the use case, we chose Lambda and Attached the policy above


##### V- Create Lambda Function

We use Python as runtime  and the role above as Execution role

##### VI- Add Trigger
* Source: S3
* Bucket: YOUR BUCKET NAME
* Event types: PUT

       <h6> Specifications</h6>
            
             - Run time: Python.x
             - Create a new role from AWS policy templates : Policy templates (Amazon S3 object read-only permissionsS3 and Amazon SNS publish policy SNS)
             - Add Trigger:
                    * source : S3 bucket
                    * Bucket name: Your Bucket Name
                    * Event Type: POST


