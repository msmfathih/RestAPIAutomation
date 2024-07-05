import requests
import time


def post_request():
    url = 'https://testing.zabehaty.uae.zabe7ti.website/api/alert-call'

    data = {
        'answExtn': '201', #201amal, 133farah
        'customerNum': '562658656'
    }

    response = requests.post(url, data=data)
    expected_status_code = 200
    if response.status_code == expected_status_code:
        print("Status code assertion passed. Status code is as expected:", expected_status_code)
    else:
        print("Status code assertion failed. Actual status code:", response.status_code)

    response_json = response.json()

    # Define the expected response data from post response body
    expected_data = {
        #'msg': 'New Customer',
        'msg': 'success'
    }

    assert response_json == expected_data, "Response body does not match expected data"
    print("Assertion passed. Response body matches expected data.")

    #validating post request size
    expected_size = 1

    assert len(
        response_json) == expected_size, (f"Response body size does not match expected size. Expected: {expected_size}"
                                          f", Actual: {len(response_json)}")
    print("Size assertion passed. Response body size matches expected size.")

    #Validating post request response time
    start_time = time.time()
    response = requests.post(url, json=data)
    end_time = time.time()
    response_time = end_time - start_time

    # Define the maximum acceptable response time in seconds
    max_response_time = 5  # Change this to the maximum acceptable response time
    # Perform assertion on the response time


    assert response_time <= max_response_time, (f"Response time exceeded maximum acceptable limit. Expected:"
                                                f" <= {max_response_time} seconds, Actual: {response_time} seconds")
    print("Response time assertion passed. Response time is within the acceptable limit.")

    headers = {
        'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>',  # Example header
        'Content-Length': '<calculated when request is sent>',
        'Connection': 'keep-alive'
    }

    # Send the POST request with defined headers and data
    response = requests.post(url, json=data, headers=headers)

    # Get the headers from the response
    response_headers = response.headers

    # Define the expected headers
    expected_headers = ['Content-Type', 'Server']  # Example headers, add more if needed

    # Perform assertion on the headers
    for header in expected_headers:
        assert header in response_headers, f"Expected header '{header}' not found in response headers"

    print("Header assertion passed. All expected headers found in the response.")


post_request()


