import requests
import json
from requests.exceptions import Timeout, HTTPError, RequestException

BASE_URL = "http://127.0.0.1:5001"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"
}

try:

    response = requests.get(f"{BASE_URL}/", headers=headers, timeout=5)
    response.raise_for_status()
    print("Health Check:", response.json())


    response2 = requests.get(f"{BASE_URL}/users", headers=headers, timeout=5)
    response2.raise_for_status()

    users = response2.json()["data"]
    print("\nAll Users:")
    print(users)


    ext_users = []
    for user in users:
        ext_users.append({"id":user["id"],"name":user["name"]})
    with open("ext_users.json", "w") as f:
        json.dump(ext_users, f, indent=4)

    print("\nData written to ext_users.json successfully")


    response3 = requests.get(f"{BASE_URL}/users/1", headers=headers, timeout=5)
    response3.raise_for_status()
    print("\nSingle User:")
    print(response3.json())


    body = {
        "name": "Reena",
        "email": "reena@example.com",
        "role": "User"
    }
    response4 = requests.post(f"{BASE_URL}/users", json=body, headers=headers, timeout=5)
    response4.raise_for_status()
    print("\nUser Created:")
    print(response4.json())

except HTTPError as e:
    print("HTTP error:", e)
except Timeout:
    print("Request timed out")
except RequestException as e:
    print("Request failed:", e)
except json.JSONDecodeError:
    print("JSON parse error")
