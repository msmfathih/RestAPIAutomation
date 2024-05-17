from memory_profiler import profile
import requests

#memory profiling using memory_profiler and requests:
@profile #profiler This w# ill allow you to capture memory usage during the execution of each test case.
def test_post_api_memory_leak():
    # Send POST requests while monitoring memory usage
    for _ in range(100):
        payload = {'emirate_id': '4',
                   'branch_id': '8'
                   }
        response = requests.post("https://testing.zabehaty.uae.zabe7ti.website/api/regions", json=payload)
        # Process response or perform assertions as needed
        assert response.status_code == 200


if __name__ == "__main__":
    test_post_api_memory_leak()