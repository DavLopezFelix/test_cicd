import requests

BASE_URL = "http://api:8000"


def test_health_status_code():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200


def test_health_body():
    response = requests.get(f"{BASE_URL}/health")
    assert response.json() == {"status": "ok"}


def test_hello_status_code():
    response = requests.get(f"{BASE_URL}/hello")
    assert response.status_code == 200


def test_hello_body():
    response = requests.get(f"{BASE_URL}/hello")
    assert response.json() == {"message": "Hello from API"}


def test_db_status_code():
    response = requests.get(f"{BASE_URL}/db-test")
    assert response.status_code == 200


def test_db_body():
    response = requests.get(f"{BASE_URL}/db-test")
    assert response.json() == {
        "status": "Database connection successful"
    }


def test_unknown_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/does-not-exist")
    assert response.status_code == 200


def test_health_content_type():
    response = requests.get(f"{BASE_URL}/health")
    assert "application/json" in response.headers["Content-Type"]


def test_hello_content_type():
    response = requests.get(f"{BASE_URL}/hello")
    assert "application/json" in response.headers["Content-Type"]


def test_health_response_time():
    response = requests.get(f"{BASE_URL}/health", timeout=2)
    assert response.elapsed.total_seconds() < 2