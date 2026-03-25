
import exercise1
import unittest

class TestFizzBuzz(unittest.TestCase):

    def ShouldReturnAString_WhenReceiveAPositiveNumber(self):
        num = 10
        self.assertEqual(fizzBuzz(num),str(num))

    def ShouldReturnAString_WhenReceiveANegativeNumber(self):
        num = -10
        self.assertEqual(fizzBuzz(num),str(num))
    
    def ShouldReturnAError_WhenNotReceiveANumber(self):
        num = "a"
        with self.assertRaises(ValueError) as error:
            fizzBuzz(num)
        self.assertEqual(str(error.exception), "no es un numero")