import unittest
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root / "Week2" / "Day4(18-12)" / "ProblemSet1"))
from HomeFederalSavingsBank import value

class TestValue(unittest.TestCase):
    def test_hello_returns_zero(self):
        self.assertEqual(value("Hello"), 0)
        self.assertEqual(value("Hello, Newman"), 0)
    
    def test_hey_variations_return_twenty(self):
        self.assertEqual(value("Hey"), 20)
        self.assertEqual(value("How you doing?"), 20)
        self.assertEqual(value("How's it going?"), 20)
    
    def test_other_greetings_return_hundred(self):
        self.assertEqual(value("Hi"), 100)
        self.assertEqual(value("Good morning"), 100)
        self.assertEqual(value("What's up?"), 100)
        self.assertEqual(value("Sup"), 100)
    
    def test_case_sensitive(self):
        self.assertEqual(value("hello"), 100)
        self.assertEqual(value("HELLO"), 100)
        self.assertEqual(value("hey"), 100)
    
    def test_empty_string(self):
        self.assertEqual(value(""), 100)

if __name__ == "__main__":
    unittest.main()
