import requests

def test_health():
    response = requests.get("http://api:8000/health")
    assert response.status_code == 201

