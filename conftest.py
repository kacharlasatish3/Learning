import pytest


@pytest.fixture(scope="session")
def get_authorization_token():
    # we will call some api to get token
    # this will execute as setup
    token = "Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34"
    yield token
    # after yield will execute as tear down / after completion of test method this will execute
    token = None

#  we have 3 scopes
# function => only it executes  for each function
# class => only it executes for each class
# session => only once it execute for session
