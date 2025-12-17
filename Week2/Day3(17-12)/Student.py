class Student:
    def __init__(self, id_student, name, age, gpa):
        self.id_student = id_student
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id_student}, Name: {self.name}, Age: {self.age}, GPA: {self.gpa}"

