import requests
import time


def validate_response_time(url, max_response_time):
    try:
        # Record the start time
        start_time = time.time()

        # Send GET request
        response = requests.get(url)

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            print("Response time:", elapsed_time, "seconds")

            # Compare response time against maximum allowed time
            if elapsed_time <= max_response_time:
                print("Response time is within the allowed limit.")
            else:
                print("Response time exceeds the allowed limit.")
        else:
            print("Error: Failed to retrieve content. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Example usage
url = "https://testing.zabehaty.uae.zabe7ti.website/api/categories"
max_response_time = 5  # Maximum allowed response time in seconds
validate_response_time(url, max_response_time)