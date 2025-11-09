import requests


def validate_put_request(url, data=None):
    try:
        # Send PUT request
        response = requests.put(url, json=data)

        # Print response details
        print(f"PUT request to {url} returned status code: {response.status_code}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("PUT request was successful.")
            # Optionally, return the response object or response JSON data
            return response.json()  # Return JSON response data
        else:
            print(f"PUT request failed with status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


url = 'https://api.example.com/resource/123'
data = {'key': 'value'}

response_data = validate_put_request(url, data)

if response_data:
    # Process the response data as needed
    print(response_data)
else:
    print("PUT request failed or encountered an error.")
