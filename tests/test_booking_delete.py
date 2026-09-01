import requests


def test_delete_booking(token, booking, base_url):
    resp2 = requests.delete(f"{base_url}/booking/{booking}",
                            headers={"Cookie": f"token={token}"},
                            timeout=10)
    assert resp2.status_code == 201


def test_delete_booking_notoken(booking, base_url):
    resp2 = requests.delete(f"{base_url}/booking/{booking}", timeout=10)
    assert resp2.status_code == 403
    resp3 = requests.get(f"{base_url}/booking/{booking}", timeout=10)
    assert resp3.status_code == 200


def test_delete_booking_verify(token, booking, base_url):
    resp2 = requests.delete(f"{base_url}/booking/{booking}",
                            headers={"Cookie": f"token={token}"},
                            timeout=10)
    assert resp2.status_code == 201
    resp3 = requests.get(f"{base_url}/booking/{booking}", timeout=10)
    assert resp3.status_code == 404
