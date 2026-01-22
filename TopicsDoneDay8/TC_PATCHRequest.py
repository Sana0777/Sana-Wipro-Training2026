import requests

PatchUrl="https://api.restful-api.dev/objects/ff8081819782e69e019be431e5732faf"

body={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

response=requests.patch(PatchUrl,json=body)
print(response.status_code)
print("PATCH Status Code")
print(response.json())