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
    
    def test_ShouldReturnAnError_WhenStringHasANewLineAtTheEnd(self):        
        with self.assertRaises(ValueError) as error:
            Add("\n")
        self.assertEqual(str(error.exception), "Invalido")
    
    def test_ShouldReturnAnError_WhenStringHasACommaAtTheEnd(self):        
        with self.assertRaises(ValueError) as error:
            Add(",")
        self.assertEqual(str(error.exception), "Invalido")
    
    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasTheCorrectFormat(self):        
        num = "//;\n1;3"
        self.assertEqual(Add(num),4)
    
    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasTheCorrectFormat2(self):        
        num = "//|\n1|2|3"
        self.assertEqual(Add(num),6)
    
    def test_ShouldReturnTheSumOfAllNumbers_WhenStringHasTheCorrectFormat3(self):        
        num = "//sep\n2sep5"
        self.assertEqual(Add(num),7)
    
    def test_ShouldReturnAnError_WhenStringHasTheCorrectFormatButUseADifferentSeparator(self):        
        num = "//|\n1|2,3"
        with self.assertRaises(ValueError) as error:
            Add(num)
        self.assertEqual(str(error.exception), "'|' expected but ',' found at position 3")
    
    def test_ShouldReturnAnError_WhenStringHasANegativeNumber(self):        
        num = "1,-2"
        with self.assertRaises(ValueError) as error:
            Add(num)
        self.assertEqual(str(error.exception), "Negative number(s) not allowed: -2")
    
    def test_ShouldReturnAnError_WhenStringHasNegativeNumbers(self):        
        num = "2,-4,-9"
        with self.assertRaises(ValueError) as error:
            Add(num)
        self.assertEqual(str(error.exception), "Negative number(s) not allowed: -4,-9")
    
    def test_ShouldReturnAllErrorsSeparateByNewLines_WhenStringHasWrongFormat(self):        
        num = "//|\n1|2,-3"
        with self.assertRaises(ValueError) as error:
            Add(num)
        self.assertEqual(str(error.exception), "Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3")