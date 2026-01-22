import requests

get1url="http://127.0.0.1:5000"

response=requests.get(get1url)
print("GET status Code")
print(response.status_code)
print("HTTP Methods--> REST API Using Flask URL")

GET2Url="http://127.0.0.1:5000/users"
response=requests.get(GET2Url)
print("\nGET all the users")
print(response.status_code)
print(response.json())

get3Url="http://127.0.0.1:5000/users/1"
print("\nGET USER ID 1")
response = requests.get(get3Url)
print(response.status_code)
print(response.json())

posturl ="http://127.0.0.1:5000/users"

body={
    "name":"Rupali"
}

response=requests.post(posturl,json=body)
print("\nPOST USER ID 3")
print(response.status_code)
print(response.json())

putUrl="http://127.0.0.1:5000/users/3"

body={
   "name":"Rupali Updated"
}
response=requests.put(putUrl,json=body)
print("\nPUT USER ID 3")
print(response.status_code)
print(response.json())

PatchUrl="http://127.0.0.1:5000/users/3"

body={
    "name": "Rupali Updated 2.0"
}

response=requests.patch(PatchUrl,json=body)
print(response.status_code)
print("\nPATCH USER ID 3")
print(response.json())

DeleteUrl="http://127.0.0.1:5000/users/3"

response=requests.delete(DeleteUrl)
print(response.status_code)
print("\nDELETE USER ID 3")
print(response.text)