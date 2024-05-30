import pytest

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_deposite_success():
    response = client.post(
        "/",
        json={
            "date": "31.01.2021",
            "periods": 6,
            "amount": 10000,
            "rate": 5.0
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10041.67,
        "28.02.2021": 10083.51,
        "31.03.2021": 10125.52,
        "30.04.2021": 10167.71,
        "31.05.2021": 10210.08,
        "30.06.2021": 10252.62
    }


class TestValidErrors:

    @pytest.mark.parametrize(
        "data, res",
        [
            (
                {
                    "date": "31/01/2021",
                    "periods": 6,
                    "amount": 10000,
                    "rate": 5.0
                },
                {
                    "error": "date error, must be in format dd.mm.YYYY"
                }
            ),
            (
                {
                    "date": "31.01.2021",
                    "periods": 0,
                    "amount": 10000,
                    "rate": 5.0
                },
                {
                    "error": "periods should be greater than or equal to 1"
                }
            ),
            (
                {
                    "date": "31.01.2021",
                    "periods": 6,
                    "amount": 100,
                    "rate": 5.0
                },
                {
                    "error": "amount should be greater than or equal to 10000"
                }
            ),
            (
                {
                    "date": "31.01.2021",
                    "periods": 6,
                    "amount": 10000,
                    "rate": 12
                },
                {
                    "error": "rate should be less than or equal to 8"
                }
            ),
        ]
    )
    def test_valid(self, data, res):
        response = client.post(
            "/",
            json=data,
        )
        assert response.status_code == 400
        assert response.json() == res
