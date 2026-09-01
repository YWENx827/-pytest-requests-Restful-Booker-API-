import requests


def test_put_booking(token, booking, base_url):
    payload_update = {
        "firstname": "new",
        "lastname": "Been",
        "totalprice": 224,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-02-23",
            "checkout": "2024-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    resp2 = requests.put(f"{base_url}/booking/{booking}",
                         headers={"Cookie": f"token={token}"},
                         json=payload_update, timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["firstname"] == "new"


def test_put_booking_notoken(booking, base_url):
    payload_update = {
        "firstname": "new",
        "lastname": "Been",
        "totalprice": 224,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-02-23",
            "checkout": "2024-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    resp2 = requests.put(f"{base_url}/booking/{booking}",
                         json=payload_update, timeout=10)
    assert resp2.status_code == 403


def test_patch_booking(token, booking, base_url):
    resp2 = requests.patch(f"{base_url}/booking/{booking}",
                           headers={"Cookie": f"token={token}"},
                           json={"totalprice": 444}, timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["totalprice"] == 444
    assert resp2.json()["firstname"] == "loi"
