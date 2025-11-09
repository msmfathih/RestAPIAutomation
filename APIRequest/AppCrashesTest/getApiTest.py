import requests
import time


def test_api_response(url):
    try:
        # Measure response time
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time

        # Assertions
        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
        response_size = len(response.content)
        assert response_size > 0, "Response size is zero"

        # Display results
        print(f"Response Time: {response_time:.3f} seconds")
        print(f"Status Code: {response.status_code}")
        print(f"Response Size: {response_size} bytes")
        print("Assertions Passed Successfully!")

    except AssertionError as e:
        print(f"Assertion Error: {e}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")


# API Endpoint
url = "https://royalfoodgallery.com/api/categories"
test_api_response(url)
