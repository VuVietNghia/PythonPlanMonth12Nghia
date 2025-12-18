import unittest
from .DeepThought import check_answer  # Relative import for PyCharm compatibility

class TestDeepThought(unittest.TestCase):
    
    def test_answer_42_number(self):
        result = check_answer("42")
        self.assertEqual(result, "Yes")
    
    def test_answer_forty_two_lowercase(self):
        result = check_answer("forty-two")
        self.assertEqual(result, "Yes")

    def test_answer_forty_two_capitalized(self):
        result = check_answer("Forty-two")
        self.assertEqual(result, "Yes")
    
    def test_wrong_answer(self):
        result = check_answer("43")
        self.assertEqual(result, "Yes")
    
    def test_empty_string(self):
        result = check_answer("")
        self.assertEqual(result, "No")

if __name__ == '__main__':
    unittest.main()