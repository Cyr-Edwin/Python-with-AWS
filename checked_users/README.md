## Creat a Lambda function to periodically check AWS IAM users, verify their attributes, delete incorrect users, and notify the security team via email.

<h6>Services used</h6>

* Lambda

* IAM 

* SES

* CloudWatch

<h6> Definition of key terms</h6>

* IAM policies

> define permissions that services or identities  can use to perform  operations in AWS.

* IAM Role

> an IAM identity that you  create in your AWS account that has specific permissions.

* CloudWatch Events

> Service that provides a near-real-time stream of events that describe changes to AWS resources.


<h5> Implementation </h5>

1 . Create Lambda Policies in AWS
 

 * CloudWatch Logs:
    - Limited: **Write**

 * AIM :
     - Limited: **READ, WRITE, List**

  * PinPoint Email:
      - Limited: **WRITE**

   * SES:
       - limited: **WRITE**

    * SES V2:
       - Limited: **Write**

    * Policy Name:
       - LambdaExecution     

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListUsers",
        "iam:GetUser",
        "iam:DeleteUser",
        "iam:ListMFADevices",
        "ses:SendEmail"
      ],
      "Resource": "*"
    }
  ]
}

```

2 - Create an AIM Role for Lambda

 * Create a role and attached LambdaExecution

 * Role name : **LambdaRoleExcution**

3 - Create Lambda function