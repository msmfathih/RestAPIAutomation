import requests
import time


def post_request():
    url = 'https://testing.zabehaty.uae.zabe7ti.website/shopapi/shops_app/login'

    data = {
        'username': 'amal',
        'password': '123456'
    }

    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body: ", json_str)
