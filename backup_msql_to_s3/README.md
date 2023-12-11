## Backup database(MSQL) and Upload it to Amazon S3 (hourly or daily)

<h6>Steps to follow</h6>

* Create a S3 bucket on AWS

* Create an IAM user with Permission to access your S3 bucket

* Export the database to backup into a file

* Upload the file into S3 bucket

* Create a script that will backup the database and upload it to S3

* Use cronjob to schedule the script to run hourly/daily

<h6> Installion of Modules</h6>

* argparse

> pip install argparse (**if not present**)

* subprocess 

> pip install subprocess(**if not pressent**)

* datime

> pip install datime (**if not present**)

* boto3

> pip install boto3 (**if not present**)

<h6> Explaination </6>

## argparse

* It is a module that allows to write command-line interfaces. 

<h6>Example:</h6>

```
# import module
import argparse
# instantiate the parser
parser = argparse.ArgumentParser(description='add numbers')
# add arguments to the parser
parser.add_argument('value_1' , type=int)
parser.add_argument('value_2',type=int)
# run the parser
args = parser.parse_args()
# add two values
sum = args.value_1 + args.value_2
# display the result
print('Total = ', sum)
# on the CLI enter:
python3 YOUR_APP_NAME 1 2
Total = 2
```

## subprocess

* It is a module that alows to run other programs or command from Python code.

<h6>Example:</h6>

```
# import module
import subprocess
# run the shell command
show_dir = subprocess.run(["dir"], shell=True, capture_output=True, text=True )
# display files or folders present in that dir
print(show_dir)
```

## datetime

* It is a module that allows to manipulate date and time.

<h6>Example:</h6>

```
# import module
import datetime
# show today date
print(datetime.date.today())
```

## boto3

* It is a module that allows to interact with AWS Services.

<h6> How to use it?</h6>

1. Set up credentions:

   - YOUR ACCESS KEY
   - YOUR SECRET KEY
   - DEFAULT REGION

2. Write  code 
```
# import the module
import boto3
# initialise the s3 service
s3 = boto3.service('s3')
# display all the s3 bucket name
for bucket in s3.buckets.all():
    print(bucket.name)
```
<h6> S3 Bucket Policy</h6>

```
{
    "Version": "2012-10-17",
    "Id": "Policy1702315882050",
    "Statement": [
        {
            "Sid": "Stmt1702315874887",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::BUCKET_NAME/*"
        }
    ]
}
```

