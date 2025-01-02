import requests


def endpoint_is_working() -> bool:
    # Send a request to the health endpoint
    try:
        response = requests.get(url="http://localhost:8080/health")
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException as e:
        return False


def test_endpoint_is_working():
    assert endpoint_is_working(), "Endpoint is not working"

