import requests
import time


def endpoint_is_working(url, max_retries: int = 5, delay: int = 1) -> bool:
    for _ in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            return True
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(delay)
    return False


def test_endpoint_is_working():
    assert endpoint_is_working(url="http://localhost:8080/health"), "Endpoint not working"

