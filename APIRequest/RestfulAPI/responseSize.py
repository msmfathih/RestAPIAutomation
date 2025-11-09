import requests


def validate_response_size(url, max_size_bytes):
    try:
        # Send GET request
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve response content
            content_size = len(response.content)

            # Compare response size against maximum size
            if content_size <= max_size_bytes:
                print("Response size is within the allowed limit.")
            else:
                print("Response size exceeds the allowed limit.")
        else:
            print("Error: Failed to retrieve content. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Example usage
url = "https://royalfoodgallery.com/api/categories"
max_size_bytes = 1024 * 1024  # 1 MB
validate_response_size(url, max_size_bytes)