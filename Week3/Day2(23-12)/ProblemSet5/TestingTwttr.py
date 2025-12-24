import unittest
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root / "Week2" / "Day5(19-12)" / "ProblemSet2"))
from Twttr import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_normal_text(self):
        self.assertEqual(remove_vowels("Twitter"), "Twttr")
        self.assertEqual(remove_vowels("Hello World"), "Hll Wrld")
    
    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")
    
    def test_only_vowels(self):
        self.assertEqual(remove_vowels("aeiou"), "")
        self.assertEqual(remove_vowels("AEIOU"), "")
    
    def test_only_consonants(self):
        self.assertEqual(remove_vowels("bcdfg"), "bcdfg")
        self.assertEqual(remove_vowels("XYZ"), "XYZ")
    
    def test_numbers_and_symbols(self):
        self.assertEqual(remove_vowels("CS50"), "CS50")
        self.assertEqual(remove_vowels("Hello123!"), "Hll123!")
        self.assertEqual(remove_vowels("@#$%"), "@#$%")
    
    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels("Programming"), "Prgrmmng")
        self.assertEqual(remove_vowels("PROGRAMMING"), "PRGRMMNG")
        self.assertEqual(remove_vowels("PyThOn"), "PyThn")

if __name__ == "__main__":
    unittest.main()