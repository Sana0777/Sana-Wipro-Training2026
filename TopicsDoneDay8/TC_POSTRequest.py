import requests

posturl ="https://api.restful-api.dev/objects"

body={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

response=requests.post(posturl,json=body)
print("POST status Code")
print(response.status_code)
print(response.json())
