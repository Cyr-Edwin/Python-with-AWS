# Removed Unattached EBS Volumes

## Services used

. Elastic Computer Service (EC2)

. Lambda Function

### Key terms definition

. **EBS Volumes** : durable block-level storage device that you can attach to your EC2 instances

### EBS Volume types

. **Solid state drive volumes (SSD)**: optimized for transactional workload (**General Purpose SSD** and **Provisioned IOPS**)

. **Hard disk drive (HDD)**: optimized for large streaming workload (**Throughput Optimized HDD** and **Cold HDD**)

### Policy attached to Lambda function (Lambda execution role)
``
{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteVolume",
        "ec2:DescribeRegions",
        "ec2:DescribeVolumes"
      ],
      "Resource": "*"
    }
  ]
}
``
#### Policy action explained

. **DeleteVolume** : API operation used to delete a volume when not longer needed

. **DescribeVolumes**: API operation used to get details such as the size of the volume, its type, the Availability Zone it's in, and its attachment status