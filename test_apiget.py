import requests
import json
import pytest
from configurations import *


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.user
def test_get_users():
    url = baseurl
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    for item in result:
        assert item["id"] is not None
        assert item["name"] is not None
        assert item["email"] is not None
        assert item["gender"] is not None


@pytest.mark.user
@pytest.mark.regression
def test_get_users_invalid_url():
    url = baseurl
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 404
