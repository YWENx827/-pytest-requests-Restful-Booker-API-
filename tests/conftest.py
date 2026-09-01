

import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def token():
    resp = requests.post(f"{BASE_URL}/auth",
                         json={"username": "admin", "password": "password123"},
                         timeout=10)
    return resp.json()["token"]

@pytest.fixture
def booking(token,base_url):
    payload = {
        "firstname": "loi",
        "lastname": "Been",
        "totalprice": 224,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    resp = requests.post(f"{base_url}/booking",
                         json=payload,
                         timeout=10)
    booking_id = resp.json()["bookingid"]
    yield booking_id
    resp2 = requests.delete(f"{base_url}/booking/{booking_id}",
                            headers={"Cookie":f"token={token}"},
                            timeout=10
    )

