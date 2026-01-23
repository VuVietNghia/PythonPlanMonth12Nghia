class Student:
    def __init__(self, id_student, name, age, gpa):
        self.id_student = id_student
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id_student}, Name: {self.name}, Age: {self.age}, GPA: {self.gpa}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, id_student, name=None, age=None, gpa=None):
        for student in self.students:
            if student.id_student == id_student:
                if name is not None:
                    student.name = name
                if age is not None:
                    student.age = age
                if gpa is not None:
                    student.gpa = gpa
                print(f"Updated student: {student}")
                return True
        print(f"Student with ID '{id_student}' not found!")
        return False

    def ranking_student(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)
        
        print("Student Ranking (by GPA):")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student}")
        
        return self.students

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.id_student != student_id]