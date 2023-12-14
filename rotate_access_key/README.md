## Write a script that will check all users' access keys and deactivate the ones that are non-compliant. Also, this script should send an email to users to rotate their access keys after 85 days. All access keys should automatically be deactivated after 90 days, which can be associated with a Jenkins job to periodically check the users access keys.

<h6>Key concepts</h6>

* **botocore.exceptions**
 
   - exceptions defined within the botocore package, a dependency of Boto3.

* **Example:**

 ```
 import boto3
import botocore.exceptions

s3 = boto3.client("s3")
try:
    s3.get_object(Bucket="Your_Bucket" , key =" YOUR_KEY")

except botocore.exceptions.ClientError as e:
      if e.response["Error"]["Code"] =="NoSuchKey":
         print("No Object")
      else:
         print(e.response)
        
 ```