# import module
import time
import subprocess
import argparse
import datetime
import boto3
'''
#####################################################
# Example:

#db-name = mysqlclear
# usernmame = admin
#password=student1234
# bucket name =mybucket1986345
################################################################

# Create an argument parser
parser = argparse.ArgumentParser()

# attach value to the parser
parser.add_argument('--database', required=True, help="DB name", type=str)
parser.add_argument('--db_user',required=True, help="DB name", type=str)
parser.add_argument('--db_password', required=True, help="DB name", type=str)
parser.add_argument('--bucket_name', required=True , help="Bucket name", type=str)
parser.add_argument('--daily_or_hourly', required=True, choices=["daily","hourly"])

# parse the arguments
args = parser.parse_args()

# get the current time
current_time = time.localtime()
# choose between daily or hourly backup
choice = args.daily_or_hourly

if choice =="daily" or choice=="hourly":
    # Get the backup file
    backup_file = f"{args.database}-{current_time.tm_year}-{current_time.tm_mday}-{current_time.tm_hour}-{current_time.tm_min}.sql"

    # use subprocess to excute the db backup command
    backup_command = f"mysqldump -u {args.db_user} -p{args.db_password} {args.database}  > {backup_file}"
    subprocess.run(backup_command, shell=True)
   
    # upload the backup file to s3
    s3 = boto3.client('s3')
    s3.upload_file(backup_file , args.bucket_name , backup_file )

else:
    raise ValueError ("Invalid option!")'''
subprocess.run('ls')
