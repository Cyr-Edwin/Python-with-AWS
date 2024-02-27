# Write a Lambda function to notify a lead that an object was upload to a S3 bucket

<h1> Service Used</h1>

* Lambda Function

* S3

* SNS

* IAM

<h1> Implimentation<h1>

1 - **Create a S3 bucket**

2 - **Create a Lambda Function**
       <h6> Specifications</h6>
            
             - Run time: Python.x
             - Create a new role from AWS policy templates : Policy templates (Amazon S3 object read-only permissionsS3 and Amazon SNS publish policy SNS)
               - Add Trigger:
                    * source : S3 bucket
                    * Bucket name: Your Bucket Name
                    * Event Type: POST


