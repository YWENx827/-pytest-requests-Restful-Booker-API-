import requests


def test_get_booking_list(base_url):
    resp = requests.get(f"{base_url}/booking", timeout=10)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_booking_detail(booking, base_url):
    resp2 = requests.get(f"{base_url}/booking/{booking}", timeout=10)
    assert resp2.status_code == 200
    assert resp2.json()["firstname"] == "loi"


def test_get_booking_not_found(base_url):
    resp = requests.get(f"{base_url}/booking/99999999", timeout=10)
    assert resp.status_code == 404
