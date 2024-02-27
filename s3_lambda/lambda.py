import json
import boto3

def lambda_handler(event, context):

    # Construct message
    message = f"An object has been uploaded to S3 bucket {event}"

    # Send message to the recipient
    sns = boto3.client('sns')
    topic_arn='YOUR_TOPIC_ARN'  # Update with your SNS topic ARN
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='S3 Upload Notification'
    )

    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
