class students:
    name="Ravi"
    age=20

s1=students()
print(s1.name)
print(s1.age)

class employees:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=employees("Sana",23)
print("Employee Name -", e1.name,"\nEmployee age-",e1.age)
