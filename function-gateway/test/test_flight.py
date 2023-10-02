import pytest
import src.flight as f


@pytest.fixture()
def sample_request():
    return {
        "airline": "az",
        "code": "123",
        "origin": "fco",
        "destination": "nce",
        "time": "121212"
    }


@pytest.fixture()
def expected_flight():
    return f.Flight(airline="az", code="123", origin="fco", destination="nce", time="121212")


def test_correct_flight_parsing(sample_request, expected_flight):
    computed_flight = f.create_from_request(sample_request)
    assert expected_flight == computed_flight
    assert "winter" == computed_flight.season
