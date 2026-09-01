import requests

def test_put_booking(token,base_url):
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
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.put(f"{base_url}/booking/{booking_id}",
                         headers = {"Cookie":f"token={token}"},
                         json=payload_update,timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["firstname"] == "new"

def test_put_booking_notoken(base_url):
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
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.put(f"{base_url}/booking/{booking_id}",
                         json=payload_update,timeout=10)
    assert resp2.status_code == 403

def test_patch_booking(token,base_url):
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
    payload_update = { "totalprice": 444,}
    resp = requests.post(f"{base_url}/booking",json=payload,timeout=10)
    booking_id = resp.json()["bookingid"]
    resp2 = requests.patch(f"{base_url}/booking/{booking_id}",
                         headers = {"Cookie":f"token={token}"},
                         json=payload_update,timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["totalprice"] == 444
    assert resp2.json()["firstname"] == "loi"