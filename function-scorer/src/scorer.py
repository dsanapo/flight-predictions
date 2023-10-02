import dataclasses
import os
import logging
import jsonpickle
import boto3  # mypy: import
from aws_xray_sdk.core import patch_all

import flight
import predictor


logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

client = boto3.client('lambda')
# client.get_account_settings()


def lambda_handler(event, context):
    logger.debug('## ENV VARIABLES' + jsonpickle.encode(dict(**os.environ)))
    logger.debug('## EVENT' + jsonpickle.encode(event))
    logger.debug('## CONTEXT' + jsonpickle.encode(context))

    logger.info(f"Raw request received {event}")

    input_flight = flight.create_from_request(event)
    logger.info(f"Parsed flight: {input_flight}")

    prediction = predictor.compute_prediction(input_flight)
    logger.info(f"Computed prediction is: {prediction}")

    return dataclasses.asdict(prediction)
