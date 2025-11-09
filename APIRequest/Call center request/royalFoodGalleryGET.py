import requests
import json
import time


def validate_get_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("GET request was successful!")
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
#validate response timein get request in python fucntion?
#run the test in CMD  C:\Users\DELL\PycharmProjects\Zabehaty Admin\APIRequest\Call center request  type: python royalFoodGalleryGET.py

def validate_getrequest_respose_time(url):
    try:
        start_time = time.time()  # Record the start time
        response = requests.get(url)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        if response.status_code == 200:
            print("GET request was successful!")
            print(f"Response time: {elapsed_time} seconds")
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


def validate_response_size(url, expected_size):
    global response
    try:
        # Send the GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Calculate the size of the response content
            response_size = len(response.content)

            # Compare the actual response size with the expected size
            if response_size == expected_size:
                print("Response size validation successful.")
            else:
                print(f"Response size validation failed. Expected size: {expected_size}, Actual size: {response_size}")
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


def validate_response_body_contains(url, expected_content):
    try:
        # Send the GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Check if the expected content is present in the response text
            if expected_content in response.text:
                print("Expected content is present in the response body.")
            else:
                print("Expected content is not present in the response body.")
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


# Example usage
url = 'https://royalfoodgallery.com/api/categories'
validate_get_request(url)
validate_getrequest_respose_time(url)

expected_size = 2000  # Set the expected size of the response content
validate_response_size(url, expected_size)

expected_content = 'Huawei'  # Specify the expected content
validate_response_body_contains(url, expected_content)
