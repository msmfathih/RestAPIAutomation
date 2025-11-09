import requests
import time


def load_test_api(url, method="GET", num_requests=10):
    response_times = []

    for i in range(num_requests):
        start_time = time.time()

        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json={"key": "value"})
        else:
            raise ValueError("Unsupported HTTP method!")

        elapsed_time = time.time() - start_time
        response_times.append(elapsed_time)

        print(f"Request {i + 1}: {elapsed_time:.4f} sec, Status: {response.status_code}")

    avg_time = sum(response_times) / len(response_times)
    print(f"\nAverage Response Time: {avg_time:.4f} sec")


# Example Usage
load_test_api("https://royalfoodgallery.com/api/categories", method="GET", num_requests=14)