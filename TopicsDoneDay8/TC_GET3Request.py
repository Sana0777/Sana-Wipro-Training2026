import requests

get3Url="https://api.restful-api.dev/objects/7"
print("GET 3 Status Code")
response = requests.get(get3Url)
print(response.status_code)
print(response.json())