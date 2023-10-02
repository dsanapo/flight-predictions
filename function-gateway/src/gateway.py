import os
import logging
import json
import jsonpickle
import boto3  # mypy: import
from aws_xray_sdk.core import patch_all
import flight

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

client = boto3.client('lambda')


def lambda_handler(event, context):
    logger.debug('## ENV VARIABLES' + jsonpickle.encode(dict(**os.environ)))
    logger.debug('## EVENT' + jsonpickle.encode(event))
    logger.debug('## CONTEXT' + jsonpickle.encode(context))

    input_flight = flight.create_from_request(event)
    logger.info(f"Parsed flight: {input_flight}")

    # TODO: Add env variable for function
    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:819883234898:function:ml-scorer-function-8DxH1AHeW5x1',
        InvocationType='RequestResponse',
        Payload=json.dumps(input_flight.to_dict())
    )

    logger.info(f"Received message: {response}")
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    logger.info(f"Status Code: {status_code}")

    payload = json.loads(response['Payload'].read())
    logger.info(f"Payload: {payload}")

    return payload
