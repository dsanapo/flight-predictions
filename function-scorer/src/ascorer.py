# mypy: disable-error-code="attr-defined"

import logging
from . import flight
from . import predictor

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    event = req.get_json()
    logging.info(f"Raw request received {event}")

    input_flight = flight.create_from_request(event)
    logging.info(f"Parsed flight: {input_flight}")

    prediction = predictor.compute_prediction(input_flight)
    logging.info(f"Computed prediction is: {prediction}")

    return func.HttpResponse(
        prediction.to_json(),
        status_code=200
    )
