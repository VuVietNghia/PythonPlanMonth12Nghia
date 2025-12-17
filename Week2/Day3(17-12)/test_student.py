from Student import Student, StudentManager

manager = StudentManager()

print("=== ADDING STUDENTS ===")
manager.add_student(Student("SV001", "Vũ Việt Nghĩa", 20, 3.5))
manager.add_student(Student("SV002", "Mai Thái Dương", 21, 3.8))
manager.add_student(Student("SV003", "Trần Thủy Tiên", 19, 3.2))
manager.add_student(Student("SV004", "Lưu Sơn Trường", 22, 3.9))

print("\nCurrent students:")
for student in manager.students:
    print(f"  {student}")

print("\n=== UPDATING STUDENT ===")
manager.update_student("SV003", name="Trần Thủy Tiên", gpa=4.0)
manager.update_student("SV999")

print("\n=== RANKING STUDENTS ===")
manager.ranking_student()
