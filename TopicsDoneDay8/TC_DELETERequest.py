import requests

DeleteUrl="https://api.restful-api.dev/objects/ff8081819782e69e019be3fa116f2deb"

response=requests.delete(DeleteUrl)
print(response.status_code)
print("DELETE Status Code")
print(response.text)