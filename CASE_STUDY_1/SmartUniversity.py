import csv
import os

class Person:
    def __init__(self, p_id, name, department):
        self.p_id = p_id
        self.name = name
        self.department = department


class Student(Person):
    def __init__(self, s_id, name, department, semester, marks):
        super().__init__(s_id, name, department)
        self.semester = semester
        self.marks = marks

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


class Faculty(Person):
    def __init__(self, f_id, name, department, salary):
        super().__init__(f_id, name, department)
        self.salary = salary


class Course:
    def __init__(self, c_id, name, credits, faculty):
        self.c_id = c_id
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


class University:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.init_files()
        self.load_faculty_from_csv()
        self.load_students_from_csv()
        self.load_courses_from_csv()
        self.admin_credentials = {
            "F101": "admin123",
            "F102": "root123"
        }

    def init_files(self):
        if not os.path.exists("students_output_report.csv"):
            with open("students_output_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Department", "Semester", "Marks", "Average", "Grade"])

        if not os.path.exists("faculty_output_report.csv"):
            with open("faculty_output_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Department", "Salary"])

        if not os.path.exists("courses_output_report.csv"):
            with open("courses_output_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Course Code", "Course Name", "Credits", "Faculty"])

    def admin_login(self):
        print("\nAdmin Authentication Required")
        fid = input("Enter Faculty ID: ")
        pwd = input("Enter Password: ")

        if fid in self.admin_credentials and self.admin_credentials[fid] == pwd:
            print("Validation Successful")
            return True
        else:
            print("Access Denied: Admin privileges required")
            return False

    def add_students(self, student):
        if student.p_id in self.students:
            print("\nError: Student ID already exists!")
            return

        self.students[student.p_id] = student

        avg, grade = student.calculate_performance()
        try:
            with open("students_output_report.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    student.p_id,
                    student.name,
                    student.department,
                    student.semester,
                    "|".join(map(str, student.marks)),
                    avg,
                    grade
                ])
        except IOError:
            print("File error while saving student data.")

        print("\nStudent Added Successfully")
        print("--------------------------------")
        print("ID :", student.p_id)
        print("Name :", student.name)
        print("Department :", student.department)
        print("Semester :", student.semester)
        print("Marks :", student.marks)

    def load_students_from_csv(self):
        if not os.path.exists("students_output_report.csv"):
            return

        with open("students_output_report.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sid = row["ID"]
                marks = list(map(int, row["Marks"].split("|")))
                self.students[sid] = Student(
                    sid,
                    row["Name"],
                    row["Department"],
                    int(row["Semester"]),
                    marks
                )

    def load_courses_from_csv(self):
        if not os.path.exists("courses_output_report.csv"):
            return

        with open("courses_output_report.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                faculty_name = row["Faculty"]

                # Find faculty object by name
                faculty_obj = None
                for fac in self.faculty.values():
                    if fac.name == faculty_name:
                        faculty_obj = fac
                        break

                if faculty_obj:
                    self.courses[row["Course Code"]] = Course(
                        row["Course Code"],
                        row["Course Name"],
                        int(row["Credits"]),
                        faculty_obj
                    )

    def load_faculty_from_csv(self):
        if not os.path.exists("faculty_output_report.csv"):
            return

        with open("faculty_output_report.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.faculty[row["ID"]] = Faculty(
                    row["ID"],
                    row["Name"],
                    row["Department"],
                    float(row["Salary"])
                )

    def delete_student(self, sid):
        if sid not in self.students:
            print("\nError: Student ID does not exist!")
            return

        del self.students[sid]

        with open("students_output_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Semester", "Marks"])
            for s in self.students.values():
                writer.writerow([
                    s.p_id,
                    s.name,
                    s.department,
                    s.semester,
                    s.marks
                ])

        print("\nStudent Deleted Successfully")

    def add_faculty(self, faculty):
        if faculty.p_id in self.faculty:
            print("\nError: Faculty ID already exists!")
            return

        self.faculty[faculty.p_id] = faculty

        with open("faculty_output_report.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                faculty.p_id,
                faculty.name,
                faculty.department,
                faculty.salary
            ])

        print("\nFaculty Added Successfully")
        print("--------------------------------")
        print("ID :", faculty.p_id)
        print("Name :", faculty.name)
        print("Department :", faculty.department)
        print("Salary :", faculty.salary)

    def add_courses(self, course):
        if course.c_id in self.courses:
            print("\nError: Course Code already exists!")
            return

        self.courses[course.c_id] = course

        with open("courses_output_report.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                course.c_id,
                course.name,
                course.credits,
                course.faculty.name
            ])

        print("\nCourse Added Successfully")
        print("--------------------------------")
        print("Course Code :", course.c_id)
        print("Course Name :", course.name)
        print("Credits :", course.credits)
        print("Faculty :", course.faculty.name)

    def enroll_student(self, sid, cid):
        if sid in self.students and cid in self.courses:
            print("\nEnrollment Successful")
            print("Student :", self.students[sid].name)
            print("Course :", self.courses[cid].name)
        else:
            print("Invalid Student ID or Course Code")

    def generate_student_report(self):
        if not self.students:
            print("No student records found.")
            return
        print("\nStudents Record Generated Successfully :")
        print("-------------------------------------------")

        for sid, student in self.students.items():
            avg, grade = student.calculate_performance()
            print(f"{sid:<8} - {student.name:<20} - {student.department:<10} - {avg:<6.2f} - {grade}")
    def generate_faculty_report(self):
        if not self.faculty:
            print("No faculty records found.")
            return
        print("\nFaculty Record Generated Successfully :")
        print("-------------------------------------------")

        for fid,faculty in self.faculty.items():
            print(f"{fid:<8} {faculty.name:<20} {faculty.department}")

    def generate_course_report(self):
        if not self.courses:
            print("No course records found.")
            return
        print("\nCourse Record Generated Successfully :")
        print("-------------------------------------------")

        for cid,course in self.courses.items():
            print(f"{cid:<10} {course.name:<20} {course.credits:<8} {course.faculty.name}")

obj = University()

while True:
    print("\nSMART UNIVERSITY MANAGEMENT SYSTEM")
    print("----------------------------------")
    print("1 → Add Student")
    print("2 → Add Faculty")
    print("3 → Add Course")
    print("4 → Enroll Student to Course")
    print("5 → Calculate Student Performance")
    print("6 → Compare Two Students")
    print("7 → Generate Reports")
    print("8 → Find All the Faculty Available")
    print("9 → Find Available Courses")
    print("10 → Delete Student")
    print("11 → Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        if not obj.admin_login():
            continue
        sid = input("Student ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        try:
            marks = list(map(int, input("Enter marks (space separated): ").split()))
        except ValueError:
            print("Invalid marks format. Please enter numbers only.")
            continue
        obj.add_students(Student(sid, name, dept, sem, marks))

    elif choice == 2:
        if not obj.admin_login():
            continue
        fid = input("Faculty ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = float(input("Salary: "))
        obj.add_faculty(Faculty(fid, name, dept, salary))

    elif choice == 3:
        if not obj.admin_login():
            continue
        cid = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fid = input("Faculty ID: ")

        if fid not in obj.faculty:
            print("Error: Faculty ID does not exist!")
        else:
            obj.add_courses(Course(cid, name, credits, obj.faculty[fid]))

    elif choice == 4:
        sid = input("Student ID: ")
        cid = input("Course Code: ")
        obj.enroll_student(sid, cid)

    elif choice == 5:
        sid = input("Student ID: ")
        if sid in obj.students:
            avg, grade = obj.students[sid].calculate_performance()
            print("Name:",obj.students[sid].name)
            print("Marks:",obj.students[sid].marks)
            print("Average:", avg)
            print("Grade:", grade)
        else:
            print("Student ID not found")

    elif choice == 6:
        s1 = input("First Student ID: ")
        s2 = input("Second Student ID: ")
        if s1 in obj.students and s2 in obj.students:
            print(f"{obj.students[s1].name}'s Marks > {obj.students[s2].name}'s Marks :", obj.students[s1] > obj.students[s2])
        else:
            print("Invalid Student IDs")
    elif choice == 7:
        obj.generate_student_report()
    elif choice == 8:
        obj.generate_faculty_report()

    elif choice == 9:
        obj.generate_course_report()

    elif choice == 10:
        if not obj.admin_login():
            continue
        sid = input("Enter Student ID to delete: ")
        obj.delete_student(sid)

    elif choice == 11:
        print("\nTHANK YOU FOR USING SMART UNIVERSITY MANAGEMENT SYSTEM")
        break

    else:
        print("Invalid Choice! Please choose the numbers from Menu System")
