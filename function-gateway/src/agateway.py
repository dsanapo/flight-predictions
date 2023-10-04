# mypy: disable-error-code="attr-defined,import"
import logging
# import os
import requests
import azure.functions as func

from . import flight


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # phase = os.environ['PHASE']
    # scoring_service_key = os.environ['SCORING_SERVICE_KEY']

    event = req.get_json()
    logging.info(f"Raw request received {event}")

    input_flight = flight.create_from_request(event)
    logging.info(f"Parsed flight: {input_flight}")

    url = 'https://flightprediction.azurewebsites.net/api/function-scorer'
    response = requests.post(url, data=input_flight.to_json(), timeout=10)

    return func.HttpResponse(
        response.text,
        status_code=200
    )
