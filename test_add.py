"""
Test_add
"""
from exercise2 import(
    Add
)

import unittest

class TestAdd(unittest.TestCase):

    def test_ShouldReturnZero_WhenStringIsEmpty(self):
        num = ""
        self.assertEqual(Add(num),0)
    
    def test_ShouldReturnTheSameNumber_WhenStringIsOneNumber(self):
        num = "1"
        self.assertEqual(Add(num),1)
    
    def test_ShouldReturnTheSumOfBothNumbers_WhenStringIsUptoTwoNumbers(self):
        num = "1,2"
        self.assertEqual(Add(num),3)

    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasManyNumbers(self):
        num = "2,1,4,5,7"
        self.assertEqual(Add(num),19)
    
    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasNewLinesAsSeparators(self):
        num = "1,2\n3"
        self.assertEqual(Add(num),6)
    
    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasANewLineSeparatorFollowingComa(self):
        num = "2,\n3"
        self.assertEqual(Add(num),5)