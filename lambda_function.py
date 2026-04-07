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

    # extract location + noise type from filename
    filename = key.lower()
    try:
        parts = filename.split("_")
        location = parts[0].capitalize()
        noise_type = parts[1].split(".")[0].capitalize()
    except:
        location = "Unknown"
        noise_type = "Unknown"

    # cleanup location format
    if location.startswith("area"):
        location = "Area " + location[-1].upper()

    fake_text = f"{noise_type} noise reported"

    item = {
        "id": str(uuid.uuid4()),
        "file": key,
        "text": fake_text,
        "location": location,
        "noise_type": noise_type,
        "timestamp": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    # count + collect noise types
    response = table.scan()

    count = 0
    noise_types = set()

    for item in response['Items']:
        if item.get('location') == location:
            count += 1
            noise_types.add(item.get('noise_type'))

    print("Total reports:", count)

    #  show all noise types
    if count == 3:
        noise_list = ", ".join(noise_types)

        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=f"High noise reported in {location}: {noise_list} ({count} reports)",
            Subject="Noise Alert"
        )
        print("SNS alert sent!")

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }
