# Import module
import boto3

# Launch EC2 service
ec2 = boto3.resource("ec2")

# Create EC2 instance
def create_ec2_instance():
    try:
        instances = ec2.create_instances(
        ImageId="ami-0fa1ca9559f1892ec",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2_key_pair"
        )
        print("EC2 instance created!\n\n")


    except Exception as e:
        print(e)

# Retrieve instance IDS
def instance_id():

    try:
        i_d = ec2.instances.all()
        for instance in i_d:
            print(instance.id)
            
    except Exception as e:
        print(e)

create_ec2_instance()
instance_id()