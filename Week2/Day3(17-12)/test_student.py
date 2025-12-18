"""
Unit Test cho Student.py

Sử dụng 2 kỹ thuật kiểm thử:
1. Phân vùng tương đương (Equivalence Partitioning - EP):
   - Chia input thành các nhóm có hành vi tương tự
   - Test 1 đại diện từ mỗi nhóm

2. Giá trị biên (Boundary Value Analysis - BVA):
   - Test các giá trị ở biên của mỗi phân vùng
   - Ví dụ: GPA có range 0.0-4.0 → test 0.0, 4.0, -0.1, 4.1
"""

import unittest
from . import Student


class TestAddStudent(unittest.TestCase):
    """
    Test add_student() với 5 test cases:
    
    Phân vùng tương đương:
    - EP1: Student hợp lệ với dữ liệu chuẩn
    - EP2: Student với GPA ở giới hạn
    - EP3: Student với age ở giới hạn
    
    Giá trị biên:
    - BVA1: GPA = 0.0 (biên dưới)
    - BVA2: GPA = 4.0 (biên trên)
    - BVA3: Age = 18 (tuổi tối thiểu thực tế)
    """
    
    def setUp(self):
        """Khởi tạo StudentManager mới cho mỗi test."""
        self.manager = Student.StudentManager()
    
    # Test Case 1: EP - Valid student với dữ liệu chuẩn
    def test_add_valid_student_normal_data(self):
        """
        [EP] Thêm sinh viên với dữ liệu hợp lệ tiêu chuẩn.
        Expected: Danh sách có 1 sinh viên.
        """
        student = Student.Student("SV001", "Nguyen Van A", 20, 3.5)
        self.manager.add_student(student)
        
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(self.manager.students[0].name, "Nguyen Van A")
    
    # Test Case 2: BVA - GPA ở biên dưới (0.0)
    def test_add_student_with_min_gpa_boundary(self):
        """
        [BVA] Thêm sinh viên với GPA = 0.0 (giá trị biên dưới).
        Expected: Sinh viên được thêm thành công với GPA = 0.0
        """
        student = Student("SV002", "Le Van B", 22, 0.0)
        self.manager.add_student(student)
        
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(self.manager.students[0].gpa, 0.0)
    
    # Test Case 3: BVA - GPA ở biên trên (4.0)
    def test_add_student_with_max_gpa_boundary(self):
        """
        [BVA] Thêm sinh viên với GPA = 4.0 (giá trị biên trên).
        Expected: Sinh viên được thêm thành công với GPA = 4.0
        """
        student = Student("SV003", "Tran Thi C", 21, 4.0)
        self.manager.add_student(student)
        
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(self.manager.students[0].gpa, 4.0)
    
    # Test Case 4: EP - Thêm nhiều sinh viên liên tiếp
    def test_add_multiple_students(self):
        """
        [EP] Thêm nhiều sinh viên liên tiếp.
        Expected: Danh sách chứa đúng số lượng sinh viên đã thêm.
        """
        students = [
            Student("SV001", "Nguyen Van A", 20, 3.5),
            Student("SV002", "Le Van B", 21, 3.0),
            Student("SV003", "Tran Thi C", 22, 3.8),
        ]
        
        for student in students:
            self.manager.add_student(student)
        
        self.assertEqual(len(self.manager.students), 3)
    
    # Test Case 5: BVA - Age ở biên (tuổi 18 - tuổi tối thiểu sinh viên)
    def test_add_student_with_min_age_boundary(self):
        """
        [BVA] Thêm sinh viên với age = 18 (tuổi biên dưới hợp lệ).
        Expected: Sinh viên được thêm thành công với age = 18
        """
        student = Student.Student("SV004", "Pham Van D", 18, 3.2)
        self.manager.add_student(student)
        
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(self.manager.students[0].age, 18)


class TestUpdateStudent(unittest.TestCase):
    """
    Test update_student() với 5 test cases:
    
    Phân vùng tương đương:
    - EP1: ID tồn tại, update thành công
    - EP2: ID không tồn tại
    - EP3: Update một field duy nhất
    - EP4: Update nhiều field cùng lúc
    
    Giá trị biên:
    - BVA1: Update GPA về 0.0 (biên dưới)
    - BVA2: Update GPA về 4.0 (biên trên)
    """
    
    def setUp(self):
        """Khởi tạo StudentManager với dữ liệu mẫu."""
        self.manager = StudentManager()
        self.manager.add_student(Student("SV001", "Nguyen Van A", 20, 3.5))
        self.manager.add_student(Student("SV002", "Le Van B", 21, 3.0))
    
    # Test Case 1: EP - Update với ID tồn tại
    def test_update_existing_student_single_field(self):
        """
        [EP] Update tên của sinh viên có ID tồn tại.
        Expected: Return True, tên được cập nhật.
        """
        result = self.manager.update_student("SV001", name="Nguyen Van A Updated")
        
        self.assertTrue(result)
        self.assertEqual(self.manager.students[0].name, "Nguyen Van A Updated")
    
    # Test Case 2: EP - Update với ID không tồn tại
    def test_update_nonexistent_student(self):
        """
        [EP] Update sinh viên với ID không tồn tại.
        Expected: Return False, không có thay đổi.
        """
        result = self.manager.update_student("SV999", name="Unknown")
        
        self.assertFalse(result)
        # Đảm bảo danh sách không thay đổi
        self.assertEqual(len(self.manager.students), 2)
    
    # Test Case 3: EP - Update nhiều field cùng lúc
    def test_update_multiple_fields(self):
        """
        [EP] Update nhiều field (name, age, gpa) cùng lúc.
        Expected: Tất cả các field được cập nhật đúng.
        """
        result = self.manager.update_student(
            "SV001", 
            name="Tran Van X", 
            age=25, 
            gpa=3.9
        )
        
        self.assertTrue(result)
        student = self.manager.students[0]
        self.assertEqual(student.name, "Tran Van X")
        self.assertEqual(student.age, 25)
        self.assertEqual(student.gpa, 3.9)
    
    # Test Case 4: BVA - Update GPA về biên dưới (0.0)
    def test_update_gpa_to_min_boundary(self):
        """
        [BVA] Update GPA về giá trị biên dưới = 0.0
        Expected: GPA được cập nhật thành 0.0
        """
        result = self.manager.update_student("SV002", gpa=0.0)
        
        self.assertTrue(result)
        self.assertEqual(self.manager.students[1].gpa, 0.0)
    
    # Test Case 5: BVA - Update GPA về biên trên (4.0)
    def test_update_gpa_to_max_boundary(self):
        """
        [BVA] Update GPA về giá trị biên trên = 4.0
        Expected: GPA được cập nhật thành 4.0
        """
        result = self.manager.update_student("SV001", gpa=4.0)
        
        self.assertTrue(result)
        self.assertEqual(self.manager.students[0].gpa, 4.0)


class TestRemoveStudent(unittest.TestCase):
    """
    Test remove_student() với 5 test cases:
    
    Phân vùng tương đương:
    - EP1: Xóa sinh viên có ID tồn tại
    - EP2: Xóa sinh viên với ID không tồn tại
    - EP3: Xóa sinh viên cuối cùng trong danh sách
    
    Giá trị biên:
    - BVA1: Xóa khi danh sách chỉ có 1 sinh viên
    - BVA2: Xóa khi danh sách rỗng
    """
    
    def setUp(self):
        """Khởi tạo StudentManager với dữ liệu mẫu."""
        self.manager = StudentManager()
    
    # Test Case 1: EP - Xóa sinh viên có ID tồn tại
    def test_remove_existing_student(self):
        """
        [EP] Xóa sinh viên có ID tồn tại trong danh sách.
        Expected: Danh sách giảm 1 sinh viên, sinh viên bị xóa không còn.
        """
        self.manager.add_student(Student("SV001", "Nguyen Van A", 20, 3.5))
        self.manager.add_student(Student("SV002", "Le Van B", 21, 3.0))
        
        self.manager.remove_student("SV001")
        
        self.assertEqual(len(self.manager.students), 1)
        # Đảm bảo sinh viên đúng bị xóa
        remaining_ids = [s.id_student for s in self.manager.students]
        self.assertNotIn("SV001", remaining_ids)
        self.assertIn("SV002", remaining_ids)
    
    # Test Case 2: EP - Xóa sinh viên với ID không tồn tại
    def test_remove_nonexistent_student(self):
        """
        [EP] Xóa sinh viên với ID không tồn tại.
        Expected: Danh sách không thay đổi.
        """
        self.manager.add_student(Student("SV001", "Nguyen Van A", 20, 3.5))
        original_count = len(self.manager.students)
        
        self.manager.remove_student("SV999")
        
        self.assertEqual(len(self.manager.students), original_count)
    
    # Test Case 3: BVA - Xóa khi danh sách chỉ có 1 sinh viên
    def test_remove_only_student_boundary(self):
        """
        [BVA] Xóa sinh viên duy nhất trong danh sách (biên: size = 1 → 0).
        Expected: Danh sách trở nên rỗng.
        """
        self.manager.add_student(Student("SV001", "Nguyen Van A", 20, 3.5))
        
        self.manager.remove_student("SV001")
        
        self.assertEqual(len(self.manager.students), 0)
    
    # Test Case 4: BVA - Xóa khi danh sách rỗng
    def test_remove_from_empty_list_boundary(self):
        """
        [BVA] Xóa từ danh sách rỗng (biên: size = 0).
        Expected: Không có lỗi, danh sách vẫn rỗng.
        """
        # Danh sách đã rỗng từ setUp
        self.manager.remove_student("SV001")
        
        self.assertEqual(len(self.manager.students), 0)
    
    # Test Case 5: EP - Xóa sinh viên cuối cùng trong danh sách (theo thứ tự)
    def test_remove_last_student_in_list(self):
        """
        [EP] Xóa sinh viên ở vị trí cuối cùng trong danh sách.
        Expected: Sinh viên cuối bị xóa, các sinh viên khác còn lại.
        """
        self.manager.add_student(Student("SV001", "Nguyen Van A", 20, 3.5))
        self.manager.add_student(Student("SV002", "Le Van B", 21, 3.0))
        self.manager.add_student(Student("SV003", "Tran Thi C", 22, 3.8))
        
        self.manager.remove_student("SV003")
        
        self.assertEqual(len(self.manager.students), 2)
        remaining_ids = [s.id_student for s in self.manager.students]
        self.assertNotIn("SV003", remaining_ids)


if __name__ == "__main__":
    # Chạy tất cả test với output chi tiết
    unittest.main(verbosity=2)
