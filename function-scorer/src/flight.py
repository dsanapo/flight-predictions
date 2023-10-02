""" Module responsible of building the enriched flight (from input request).
"""
# mypy: disable-error-code="attr-defined"
# https://github.com/lidatong/dataclasses-json/issues/23
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json


@dataclass_json
@dataclass
class Flight:
    airline: str
    code: str
    origin: str
    destination: str
    time: str
    season: str
    weather_alert: str


def create_from_request(flight: dict) -> Flight:
    """
    Reads the configuration file and create the config objects.
    :param flight: input flight as string
    :return: the created flight
    :rtype:
    """
    json_object = json.dumps(flight)
    return Flight.from_json(json_object)
