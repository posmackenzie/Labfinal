import json
import boto3

from datetime import datetime

def handler(event, context):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")

        sqs = boto3.client('sqs')
        sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/691758086353/pos-queue',
        MessageBody='Test send message'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(current_time)
                        } 