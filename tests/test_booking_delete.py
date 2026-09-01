

import requests

def test_delete_booking(token,base_url):
    payload ={
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
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.delete(f"{base_url}/booking/{booking_id}",
                         headers = {"Cookie":f"token={token}"},
                         timeout=10)
    assert resp2.status_code == 201

def test_delete_booking_notoken(base_url):
    payload ={
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
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.delete(f"{base_url}/booking/{booking_id}",
                         timeout=10)
    assert resp2.status_code == 403
    resp3 = requests.get(f"{base_url}/booking/{booking_id}",timeout=10)
    assert resp3.status_code == 200

def test_delete_booking_verify(token,base_url):
    payload ={
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
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.delete(f"{base_url}/booking/{booking_id}",
                            headers= {"Cookie":f"token={token}"},
                            timeout=10)
    assert resp2.status_code == 201
    resp3 = requests.get(f"{base_url}/booking/{booking_id}",timeout=10)
    assert resp3.status_code == 404