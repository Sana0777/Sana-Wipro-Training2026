class Student:
    def student_info(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display_details(self):
        print(f"Name is {self.name} and Roll no. is {self.rollno}")

obj1=Student()
obj1.student_info("Sana Bano",101)
obj1.display_details()
obj1.student_info("Shifa Bano",102)
obj1.display_details()