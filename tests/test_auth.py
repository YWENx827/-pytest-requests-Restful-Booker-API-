
import requests


def test_auth_success(token):
    assert token != ""

def test_auth_wrong_password(base_url):
    resp = requests.post(f"{base_url}/auth",
                         json={"username": "admin", "password": "wrong"},
                         timeout=10)
    assert "reason" in resp.json()

