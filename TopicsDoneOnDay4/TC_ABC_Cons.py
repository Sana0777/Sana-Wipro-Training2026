from abc import ABC ,abstractmethod

class Employee:
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass
class Manager(Employee):
    def salary(self):
        print(self.name,"Your salary is 50,000")
obj=Manager("Sana")
obj.salary()