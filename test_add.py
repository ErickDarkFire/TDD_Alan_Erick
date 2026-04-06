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