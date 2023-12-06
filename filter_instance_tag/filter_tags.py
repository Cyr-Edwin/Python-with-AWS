# import modules
import boto3

# initiate EC2 service
ec2 = boto3.resource("ec2")

# find the instance
def look_for_instance(name , value):
    # create an empty list of instances
    instance_list = []
    # key search
    filters =[
        {
            'Name': name,
            'Values': [value,]
        },
    ]
    # filter  the instance
    instances = ec2.instances.filter(Filters=filters)

    for i in instances:
     # add instancces to the empty list
     instance_list.append(i)

    return instance_list

# show details of the instance
def show_instance_details(ec2_instance):
   
   for instance in ec2_instance:
      print("instance ID:" , instance.id + "\n")
      print("instance Type: ", instance.instance_type + "\n")
      print("instance Image ID: "+ instance.image_id + "\n")

# example of tag
name='tag:Name'
value = 'ec2'

instance_list = look_for_instance(name, value)
look_for_instance(name , value)
show_instance_details(instance_list)