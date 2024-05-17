import requests


def validate_response_code(url):
    try:
        # Send GET request
        response = requests.get(url)

        # Check the status code
        if response.status_code == 200:
            print("GET request successful. Status code:", response.status_code)
        else:
            print("GET request failed. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Example usage
url = "https://royalfoodgallery.com/api/categories"
validate_response_code(url)