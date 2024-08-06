import requests
import psutil
import time


# Function to monitor memory usage
def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss  # RSS (Resident Set Size) in bytes


# URL for the GET request
url = "https://royalfoodgallery.com/api/categories"

# Number of iterations for the test
iterations = 1

# Time interval between requests in seconds
interval = 1

print("Starting memory leak test...")

# Initial memory usage
initial_memory = get_memory_usage()
print(f"Initial Memory Usage: {initial_memory / (1024 * 1024):.2f} MB")

# Perform GET requests and monitor memory usage
for i in range(iterations):
    response = requests.get(url)
    print(f"Iteration {i + 1}: Status Code {response.status_code}")

    # Check memory usage after each request
    current_memory = get_memory_usage()
    print(f"Current Memory Usage: {current_memory / (1024 * 1024):.2f} MB")

    # Sleep to simulate intervals between requests
    time.sleep(interval)

# Final memory usage
final_memory = get_memory_usage()
print(f"Final Memory Usage: {final_memory / (1024 * 1024):.2f} MB")

# Memory usage change
memory_change = final_memory - initial_memory
print(f"Memory Usage Change: {memory_change / (1024 * 1024):.2f} MB")
