import requests

putUrl="https://api.restful-api.dev/objects/ff8081819782e69e019be3fa116f2deb"

body={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
response=requests.put(putUrl,json=body)
print("PUT status Code")
print(response.status_code)
print(response.json())