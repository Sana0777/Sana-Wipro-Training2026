import requests

url="https://api.restful-api.dev/objects"

response=requests.get(url)
print("GET status Code")
print(response.status_code)
print(response.json())
