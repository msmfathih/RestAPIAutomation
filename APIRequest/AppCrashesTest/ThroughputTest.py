import requests
import time

def throughput_test(url, duration=5):
    start_time = time.time()
    count = 0

    while time.time() - start_time < duration:
        response = requests.get(url)
        if response.status_code == 200:
            count += 1

    print(f"Throughput: {count} requests in {duration} sec ({count/duration:.2f} requests/sec)")

# Example Usage
throughput_test("https://royalfoodgallery.com/api/categories", duration=5)