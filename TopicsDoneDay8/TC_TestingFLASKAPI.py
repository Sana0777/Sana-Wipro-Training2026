import requests, json

server_url = "http://127.0.0.1:5001"
users_url = "http://127.0.0.1:5001/users"

customHeader = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"
}

server_status = requests.get(server_url, headers=customHeader)
print(server_status.status_code)
print(server_status.json())

user_data = requests.get(users_url, customHeader)
print(user_data.status_code)
response_data = user_data.json()
print(response_data['data'])
print(response_data['message'])
try:
    with open("userdump.json", 'w') as file:
        json.dump(response_data['data'], file, indent=4)

except Exception as e:
    print(f"error dumping data into file: {str(e)}")

