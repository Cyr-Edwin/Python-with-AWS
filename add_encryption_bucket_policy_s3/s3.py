# import modules
import boto3
import json
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

list_buckets = s3.list_buckets()

# retreive list of bucket's names
buckets_name = []
for bucket_name in list_buckets:
    buckets_name.append(bucket_name["Buckets"]["Name"])