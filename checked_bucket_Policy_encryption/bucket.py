# import module 
import boto3

# instantiate s3 service
s3 = boto3.client("s3")

 # list all  buckets and return a dictionary
s3_bucket_list = s3.list_buckets()

# s3_bucket_list["Buckets"] = [{'Name': 'my2345673', 

#                               'CreationDate': datetime.datetime(2023, 12, 13, 5, 31, 37, tzinfo=tzutc())
#                             }]


# check if the bucket is encrypted or not
def not_or_encrypted_bucket(bucket):
  
  for s3_bucket in s3_bucket_list[bucket]:

      # check if the bucket is ecrypted by default
      if s3.get_bucket_encryption(Bucket =s3_bucket['Name']) == "ServerSideEncryptionConfigurationNotFoundError":
        print("\n")
        print("Bucket Name: " + s3_bucket['Name'] + "\n")
        print("Encripted: No")

      else:
         print("\n")
         print( "Bucket Name: "+ s3_bucket['Name'] + "\n")
         print("Encripted: Yes")


# check if the bucket has a policy  or not
def not_or_no_bucket_policy(bucket):

   bucket_info = s3_bucket_list[bucket][0]
   bucket_name = bucket_info["Name"]

   try:
      response = s3.get_bucket_policy(Bucket= bucket_name)
      print("Bucket Name: "+ bucket_name + "\n")
      print("Policy :  Yes")
    
   except s3.exceptions.ClientError as e:
      print("\n")
      print("Bucket Name: " + bucket_name + "\n")
      print("Policy :  No" + "\n")
      print("The error trace is below: " + "\n")
      print(e)
      
   
not_or_encrypted_bucket("Buckets")
not_or_no_bucket_policy("Buckets")
  