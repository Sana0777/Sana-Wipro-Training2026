import mysql.connector

host="localhost"
user="root"
password="root"
database="wipro2026"

conn=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor=conn.cursor()
print("\nConnected to MySQL database\n")

query="SELECT * FROM wipro2026.employee where salary>50000;"

cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)


insert_query = """
INSERT INTO `wipro2026`.`employee` (`empid`, `empname`, `salary`, `department`) VALUES ('107', 'Raj', '56000', 'IT');
"""

cursor.execute(insert_query)
conn.commit()

print("\nNew employee inserted successfully")

update_query = """
UPDATE `wipro2026`.`employee`
SET `salary` = `salary` + (`salary` * 0.10)
WHERE `empid` = '105';
"""

cursor.execute(update_query)
conn.commit()

print("\nSalary updated by 10% successfully")

cursor.close()
conn.close()
print("\nConnection closed")

##part --B

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB successfully")

db=client["Company_Database"]
collection=db["Employee"]

new_employee = {
    "name": "isha",
    "department": "IT",
    "salary": 76000
}

collection.insert_one(new_employee)
print("\nNew employee inserted successfully")

print("\nEmployees in IT department:")
it_employees = collection.find({"department": "IT"})

for emp in it_employees:
    print(emp)

employee_name = "Aisha"

collection.update_one(
    {"name": employee_name},
    {"$inc": {"salary": 5000}}
)

print("\nSalary updated successfully")

client.close()
print("\nMongoDB connection closed")


