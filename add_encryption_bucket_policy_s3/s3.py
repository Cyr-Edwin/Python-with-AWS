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

# find not encrypted bucket and encrypt them
def encrypt_buckets():
    # find encrypted bucket
    for bucket_name in buckets_name:
        try:
            response = s3.get_bucket_encryption(Bucket= bucket_name) 
            # information about the server-side encrytion
            rules = response["ServerSideEncryptionConfiguration"]["Rules"]
            # display the bucket name and rules used
            print(f"Bucket Name:  {bucket_name} | Rules: {rules}\n")
        except:
            pass