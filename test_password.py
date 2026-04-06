from exercise3 import(
    passwordValidation
)

import unittest

class TestPasswordValidation(unittest.TestCase):
    def test_ShouldReturnAnError_WhenThePasswordHasLessThanEightCharacters(self):
        password = "Aa19$"
        self.assertEqual(passwordValidation(password), {
            "isValid": False,
            "errors": [
                "Pasword must be at least 8 characters"
            ]
        })

    def test_ShouldReturnAnError_WhenPasswordHasLessThanTwoNumbers(self):
        password = "Qwtefg1$"
        self.assertEqual(passwordValidation(password), {
            "isValid": False,
            "errors": [
                "The passwordd must contain at least 2 numbers"
            ]
        })
