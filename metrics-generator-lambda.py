import json
import os
import boto3
import datetime
import uuid
import random

def lambda_handler(event, context):

    kinesis = boto3.client('kinesis')
    stream = os.environ['KINESIS_IN']

    records = []

    devices = ["my-device-1", "my-device-2", "my-device-3", "my-device-4"]

    for i in range(50):
        for device in devices:

            event_type = 'INFO'
            if i % 6 == 0:
                event_type = 'ALERT'

            metric = {"date_time": datetime.datetime.now().isoformat(),
                      "device_id": device,
                      "event_type": event_type,
                      "application": "koliber-iot",
                      "id": str(uuid.uuid4()),
                      "temperature": random.randint(0, 80),
                      "humidity": random.randint(10, 90),
                      "pressure": random.randint(990, 1020)}

            data = json.dumps(metric)
            records.append({'Data': bytes(data, 'utf-8'), 'PartitionKey': 'key'})

    response = kinesis.put_records(
        StreamName=stream,
        Records=records
    )

    return response
