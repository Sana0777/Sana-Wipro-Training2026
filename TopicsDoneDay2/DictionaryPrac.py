student={
    "name":"Sana",
    "age":20,
    "subject":"Python"
}
print(student)
print(student.get("age"))

print(student.keys())
print(student.values())

student["marks"]=90
student["age"]=30

print(student)

student.popitem()
print(student)

for key in student:
    print(key,student[key])

employees={

    101:{"name":"Leena","salary":20000},
    102:{"name":"Hena","salary":30000},

}

print(employees[101]["name"])

print(student)