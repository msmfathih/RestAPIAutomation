import requests
import psutil


def check_memory_leakage(url):
    # Record memory usage before making the request
    start_memory = psutil.virtual_memory().used

    # Make the GET request
    response = requests.post(url)

    # Record memory usage after making the request
    end_memory = psutil.virtual_memory().used

    # Calculate memory usage increase
    memory_increase = end_memory - start_memory

    print("Memory increase after GET request:", memory_increase, "bytes")


# Example usage
url = "https://testing.zabehaty.uae.zabe7ti.website/api/regions"
check_memory_leakage(url)