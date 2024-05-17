from asyncio import timeout

import requests
import random
import json
import string

base_url = "https://gorest.co.in"
auth_token = "Bearer 2305667a0f4bb4ec00d51e99b0a1878e61e28bf54fb23a4150fe0188de324723"

#GET request
def get_request():
    url = base_url + "/public/v2/users/"
    print("get url:" + url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json get response body: ", json_str)
    print("Elapsed Time :", response.elapsed.total_seconds())
    print(response.cookies)


get_request()


#POST request
def post_request():
    url = base_url + "/public/v2/users/"
    print("post url:" + url)
    headers = {"Authorization" : auth_token}
    data = {
        "name": "MsmFathih123",
        "email": "sample@gmail.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url,json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body: ", json_str)
    assert "name" in json_data
    assert json_data["name"] == "MsmFathih123"

    #return user_id


#PUT request update the user
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url:" + url)
    headers = {"Authorization" : auth_token}
    data = {
        "name": "MsmFathih1",
        "email": "sample123@gmail.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json put response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "MsmFathih1"


#user_id = post_request()
#put_request(user_id)
#post_request()



#Delete request