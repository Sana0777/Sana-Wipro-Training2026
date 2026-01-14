import json

data = {
    "Name": "Sana",
    "Age": "23",
    "Location": "Bengaluru",
}

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)