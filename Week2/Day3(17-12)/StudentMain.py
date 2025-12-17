from Student import Student, StudentManager

manager = StudentManager()

manager.add_student(Student("SV001", "Vũ Việt Nghĩa", 20, 3.5))
manager.add_student(Student("SV002", "Mai Thái Dương", 21, 3.8))
manager.add_student(Student("SV003", "Trần Thủy Tiên", 19, 3.2))
manager.add_student(Student("SV004", "Lưu Sơn Trường", 22, 3.9))

for student in manager.students:
    print(f"  {student}")

manager.update_student("SV003", name="Trần Thủy Tiên", gpa=4.0)
manager.update_student("SV999")

manager.ranking_student()
