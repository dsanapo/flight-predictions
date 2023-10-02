# mypy: disable-error-code="attr-defined"
# https://github.com/lidatong/dataclasses-json/issues/23
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import uuid
import random

from flight import Flight

PREDICTIONS = [
    "ontime",
    "delayed",
    "cancelled",
    "rerouted"
]


@dataclass_json
@dataclass
class Prediction:
    """
    """
    event: str
    accuracy: float


@dataclass_json
@dataclass
class ScoredRequest:
    """
    """
    flight: Flight
    prediction: Prediction
    id: str


def compute_prediction(flight: Flight) -> ScoredRequest:
    prediction = Prediction(
        event=random.choice(PREDICTIONS),
        accuracy=random.uniform(0, 1)
    )
    return ScoredRequest(
        flight=flight,
        prediction=prediction,
        id=str(uuid.uuid4())
    )
