# to automate the rest api we will use requests module
# pip

import requests

headers = {"Content-Type": "application/json",
           "Authorization": 'Bearer 9b6266b5a84b35b0ded346afbebd585e95e3a6dc1f236be90e71e175e1a7de34'}

url = "https://gorest.co.in/public/v2/users/"
response = requests.get(url=url, headers=headers)
print(response)
result = response.json()
print(result)


