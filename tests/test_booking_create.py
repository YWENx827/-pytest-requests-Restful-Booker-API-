

import requests
import pytest

def test_create_success(base_url):
    resp = requests.post(f"{base_url}/booking",
    json={
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
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == "loi"


@pytest.mark.parametrize("price",[0,1,888,1000000])
def test_create_price(base_url,price):
    payload = {
        "firstname": "loi",
        "lastname": "Been",
        "totalprice": price,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    resp = requests.post(f"{base_url}/booking",json=payload,
                         timeout=10)
    assert "bookingid" in resp.json()

def test_creat_missing(base_url):
    payload = {
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

    assert resp.status_code == 500#bug，应该返回400
