import json
import boto3
import urllib.parse
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('noise_reports')

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:ap-south-1:006215409334:noise-alerts-v2"

def lambda_handler(event, context):
    print("Event:", event)

    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )

    fake_text = "loud construction noise"

    item = {
        "id": str(uuid.uuid4()),
        "file": key,
        "text": fake_text,
        "timestamp": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    # Count total reports
    response = table.scan()
    count = len(response['Items'])

    print("Total reports:", count)

    # If >= 3 → send alert
    if count >= 3:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=f"High noise reported! Total complaints: {count}",
            Subject="Noise Alert 🚨"
        )
        print("SNS alert sent!")

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }
