
from exercise1 import(
    fizzBuzz
)

import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_ShouldReturnAString_WhenReceiveAPositiveNumber(self):
        num = 10
        self.assertEqual(fizzBuzz(num),str(num))

    def test_ShouldReturnAString_WhenReceiveANegativeNumber(self):
        num = -10
        self.assertEqual(fizzBuzz(num),str(num))
    
    def test_ShouldReturnAError_WhenNotReceiveANumber(self):
        num = "a"
        with self.assertRaises(ValueError) as error:
            fizzBuzz(num)
        self.assertEqual(str(error.exception), "no es numero")