""" Module responsible of building the enriched flight (from input request).
"""
# mypy: disable-error-code="attr-defined"
# https://github.com/lidatong/dataclasses-json/issues/23
from dataclasses import dataclass, field
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
    season: str = field(init=False)
    weather_alert: str = field(init=False)

    def __post_init__(self):
        """
        Sets the missing field after init.
        :return:
        :rtype:
        """
        self.enrich_with_current_data()

    def enrich_with_current_data(self):
        """
        Enriches the incoming request with information from other sources.
        :return:
        :rtype:
        """
        self.season = "winter"
        self.weather_alert = "thunderstorm"


def create_from_request(flight: dict) -> Flight:
    """
    Reads the configuration file and create the config objects.
    :param flight: input flight as string
    :return: the created flight
    :rtype:
    """
    json_object = json.dumps(flight)
    return Flight.from_json(json_object)
