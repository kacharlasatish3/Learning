import requests
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user():
    url = "https://gorest.co.in/public/v2/users/"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    id = result[0]["id"]
    url = "https://gorest.co.in/public/v2/users" + "/" + str(id)
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"}

    response = requests.delete(url=url, headers=header)
    assert response.status_code == 204

@pytest.mark.regression
def test_delete_user_with_invalid_token():
    url = "https://gorest.co.in/public/v2/users" + "/" + "23434433"
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer 222121213HGJH"}

    response = requests.delete(url=url, headers=header)
    assert response.status_code == 401
