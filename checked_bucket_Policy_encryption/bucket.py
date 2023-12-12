# import module 
import boto3

# instantiate s3 service
s3 = boto3.client("s3")

# list all  buckets and return a dictionary
s3_bucket_list = s3.list_buckets()