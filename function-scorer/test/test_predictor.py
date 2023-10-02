import pytest
import sys
sys.path.append('./function-scorer/src')
import flight as f
import predictor as p


@pytest.fixture()
def sample_request():
    return {
        "airline": "az",
        "code": "123",
        "origin": "fco",
        "destination": "nce",
        "time": "121212",
        "season": "winter",
        "weather_alert": "heavy-rain"
    }


def test_compute_prediction(sample_request):
    computed_prediction = p.compute_prediction(sample_request)
    assert sample_request == computed_prediction.flight
    assert computed_prediction.prediction.event in p.PREDICTIONS
    assert 0.0 < computed_prediction.prediction.accuracy < 1.0
