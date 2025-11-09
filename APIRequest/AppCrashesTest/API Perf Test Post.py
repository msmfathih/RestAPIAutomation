import requests
import concurrent.futures
import time

# Define the API endpoint
url = 'https://royalfoodgallery.com/api/categories'

# Number of concurrent requests to send
num_requests = 100


# Function to send GET request
def send_get_request(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    return response_time, response.status_code


# Send concurrent requests and measure response times
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_get_request, url) for _ in range(num_requests)]

    response_times = []
    status_codes = []
    for future in concurrent.futures.as_completed(futures):
        response_time, status_code = future.result()
        response_times.append(response_time)
        status_codes.append(status_code)
        print(f"Request took {response_time} seconds, status code: {status_code}")





# Calculate and print performance metrics
total_time = sum(response_times)
avg_time = total_time / num_requests
max_time = max(response_times)
min_time = min(response_times)
print(f"\nPerformance Metrics:")
print(f"Total time for {num_requests} requests: {total_time} seconds")
print(f"Average time per request: {avg_time} seconds")
print(f"Maximum time for a request: {max_time} seconds")
print(f"Minimum time for a request: {min_time} seconds")
