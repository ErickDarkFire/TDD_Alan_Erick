
from exercise1 import(
    fizzBuzz
)

import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_ShouldReturnAString_WhenReceiveAPositiveNumberThatIsNotAnMultipleOfThreeOrFiveOrBoth(self):
        num = 1
        self.assertEqual(fizzBuzz(num),str(num))

    def test_ShouldReturnAString_WhenReceiveANegativeNumberThatIsNotAnMultipleOfThreeOrFiveOrBoth(self):
        num = -1
        self.assertEqual(fizzBuzz(num),str(num))
    
    def test_ShouldReturnAError_WhenNotReceiveANumber(self):
        num = "a"
        with self.assertRaises(ValueError) as error:
            fizzBuzz(num)
        self.assertEqual(str(error.exception), "no es numero")
    
    def test_ShouldReturnFizz_WhenIsMultipleOfThree(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(6), "Fizz")
        self.assertEqual(fizzBuzz(12), "Fizz")

    def test_ShouldReturnBuzz_WhenIsMultipleOfFive(self):
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(20), "Buzz")

    def test_ShouldReturnBuzz_WhenIsMultipleOfFiveAndThree(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
        self.assertEqual(fizzBuzz(150), "FizzBuzz")
