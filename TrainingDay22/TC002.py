from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB successfully")

db=client["Company_Database"]
collection=db["Employee"]

new_employee = {
    "empid":105,
    "name": "Aisha",
    "department": "IT",
    "salary": 70000
}

collection.insert_one(new_employee)

all_employees = collection.find({})

print("\nAll Employees:\n")

for emp in all_employees:
    print(emp)


client.close()