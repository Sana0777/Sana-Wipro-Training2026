import requests

GET2Url="https://api.restful-api.dev/objects?id=3&id=5&id=10"
response=requests.get(GET2Url)
print("GET Status Code")
print(response.status_code)
print(response.json())