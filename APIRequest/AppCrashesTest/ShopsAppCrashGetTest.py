from memory_profiler import profile
import requests


@profile
def test_api_memory_leak():
    # Execute API calls while monitoring memory usage
    for _ in range(100):
        response = requests.get("https://royalfoodgallery.com/api/categories")
        # Process response or perform assertions as needed
        assert response.status_code == 200


if __name__ == "__main__":
    test_api_memory_leak()
