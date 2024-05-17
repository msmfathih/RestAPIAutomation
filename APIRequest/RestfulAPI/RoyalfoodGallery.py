from asyncio import timeout
from wsgiref import headers

import requests
import random
import json
import string

base_url = "https://royalfoodgallery.com"
#auth_token = "Bearer e4531bb62d6ed17ea4ba6c40106a11b49c7878cd4d637282316975f93c7aedd4"


#GET request
def get_request():
    url = base_url + "/api/categories"
    print("get url:" + url)
    #headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json get response body: ", json_str)
    print("Elapsed Time :", response.elapsed.total_seconds())
    print(response.cookies)


get_request()