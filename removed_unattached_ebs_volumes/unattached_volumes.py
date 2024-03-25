# import Modules
import boto3

#def lambda_handler(event , context):
  # Get all Region Names  
ec2 = boto3.client('ec2')
list_of_regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]


for region in list_of_regions:
    ec2_resource = boto3.resource('ec2' , region_name=region)

    # display Region
    print(f"Rigion ==> :  {region}")

