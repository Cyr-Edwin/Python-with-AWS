# Import Module
import boto3

# Defined standard entry point
def lambda_handler(event , context):
    # Get the list of Regions
    ec2_client = boto3.client('ec2')
    
    # Empty instances 
    ec2_instances = []

    # List comprehension
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    # Iterate over each Region
    for region in regions:
        ec2 = boto3.resource('ec2' , region_name = region)

        print (f"Region: {region}")

        # Get only running EC2 instances
        ec2_instances = ec2.instances.filter([
            {'Name': 'instance-state-name',
             'Values':['running']}])
        
        # Stop running EC2 instances
        for ec2_instance in ec2_instances:
            ec2_instance.stop()
            print(f"{ec2_instance.id} : Instance Stopped")
        
        