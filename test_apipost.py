import string
import requests
import json
import random
import pytest
from configurations import *

# Pep8 standards
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.user
@pytest.mark.usefixtures("get_authorization_token")
def test_create_user(get_authorization_token):
    token = get_authorization_token
    url = baseurl
    header = {"Content-Type": "application/json",
              "Authorization": token}

    name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                  string.digits, k=10))
    email = name + "@gmail.com"
    data = json.dumps({
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    })
    response = requests.post(url, headers=header, data=data)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None
    assert result["name"] == name
    assert result["email"] == email
    assert result["gender"] == "male"
    assert result["status"] == "active"

@pytest.mark.regression
@pytest.mark.usefixtures("get_authorization_token")
def test_create_user1(get_authorization_token):
    token = get_authorization_token
    url = baseurl
    header = {"Content-Type": "application/json",
              "Authorization": token}

    name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                  string.digits, k=10))
    email = name + "@gmail.com"
    data = json.dumps({
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    })
    response = requests.post(url, headers=header, data=data)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None
    assert result["name"] == name
    assert result["email"] == email
    assert result["gender"] == "male"
    assert result["status"] == "active"



# @pytest.mark.regression
# def test_create_user_invalid_token():
#     url = baseurl
#     header = {"Content-Type": "application/json",
#               "Authorization": "Bearer 838488"}
#
#     name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
#                                   string.digits, k=10))
#     email = name + "@gmail.com"
#     data = json.dumps({
#         "name": name,
#         "email": email,
#         "gender": "male",
#         "status": "active"
#     })
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 401
#     result = response.json()
#     assert result["message"] == "Invalid token"
#
# @pytest.mark.regression
# def test_create_user_existing_email():
#     url = baseurl
#     header = {"Content-Type": "application/json",
#               "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}
#
#     name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
#                                   string.digits, k=10))
#     email = name + "@gmail.com"
#     data = json.dumps({
#         "name": name,
#         "email": email,
#         "gender": "male",
#         "status": "active"
#     })
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 201
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 422
#     result = response.json()
#     assert result[0]["field"] == "email"
#     assert result[0]["message"] == "has already been taken"
#

#
# @pytest.mark.regression
# def test_create_user_empty_name():
#     url = "https://gorest.co.in/public/v2/users"
#     header = {"Content-Type": "application/json",
#               "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}
#
#     name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
#                                   string.digits, k=10))
#     email = name + "@gmail.com"
#     data = json.dumps({
#         "name": "",
#         "email": email,
#         "gender": "male",
#         "status": "active"
#     })
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 422
#     result = response.json()
#     assert result[0]["field"] == "name"
#     assert result[0]["message"] == "can't be blank"
#
# @pytest.mark.regression
# def test_create_user_empty_email():
#     url = "https://gorest.co.in/public/v2/users"
#     header = {"Content-Type": "application/json",
#               "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}
#
#     name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
#                                   string.digits, k=10))
#     data = json.dumps({
#         "name": "asas",
#         "email": "",
#         "gender": "male",
#         "status": "active"
#     })
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 422
#     result = response.json()
#     assert result[0]["field"] == "email"
#     assert result[0]["message"] == "can't be blank"
#
# @pytest.mark.regression
# def test_create_user_empty_email_name():
#     url = "https://gorest.co.in/public/v2/users"
#     header = {"Content-Type": "application/json",
#               "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}
#
#     data = json.dumps({
#         "name": "",
#         "email": "",
#         "gender": "male",
#         "status": "active"
#     })
#     response = requests.post(url, headers=header, data=data)
#     assert response.status_code == 422
#     result = response.json()
#     assert result[0]["field"] == "email"
#     assert result[0]["message"] == "can't be blank"
#     assert result[1]["field"] == "name"
#     assert result[1]["message"] == "can't be blank"
