
import requests

def test_get_booking_list(base_url):
    resp = requests.get(f"{base_url}/booking",
                        timeout=10)
    assert resp.status_code == 200
    assert isinstance(resp.json(),list)

def test_get_booking_detail(base_url):
    payload = {
    "firstname": "loi",
    "lastname": "Been",
    "totalprice": 224,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-02-23",
        "checkout": "2024-10-23"
    },
    "additionalneeds": "Breakfast"
}
    resp = requests.post(f"{base_url}/booking",
    json=payload,
    timeout=10
    )
    booking_id = resp.json()["bookingid"]
    resp2 = requests.get(f"{base_url}/booking/{booking_id}",timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["firstname"] == "loi"

def test_get_booking_not_found(base_url):
    resp = requests.get(f"{base_url}/booking/99999999",
                        timeout=10)
    assert resp.status_code == 404