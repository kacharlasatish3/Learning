import string
import requests
import json
import random
import pytest
from configurations import *

@pytest.mark.smoke
@pytest.mark.regression
def test_update_user():
    url = baseurl
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    id = result[0]["id"]
    url = baseurl + "/" + str(id)
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}

    name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                  string.digits, k=10))
    email = name + "@gmail.com"
    data = json.dumps({
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    })
    response = requests.put(url, headers=header, data=data)
    assert response.status_code == 200
    result = response.json()
    assert result["id"] == id
    assert result["name"] == name
    assert result["email"] == email
    assert result["gender"] == "male"
    assert result["status"] == "active"


@pytest.mark.smoke
@pytest.mark.regression
def test_user_patch():

    headers = {"Content-Type": "application/json"}
    response = requests.get(url=baseurl, headers=headers)
    assert response.status_code == 200
    result = response.json()
    id = result[0]["id"]
    url = baseurl+ "/" + str(id)
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}

    name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                  string.digits, k=10))
    email = name + "@gmail.com"
    data = json.dumps({
        "name": name
    })
    response = requests.put(url, headers=header, data=data)
    assert response.status_code == 200
