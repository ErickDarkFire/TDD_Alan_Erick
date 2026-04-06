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

    def test_ShouldReturnAnError_WhenPasswordDoesNotContainACapitalLetter(self):
        password = "loikjf57$"
        self.assertEqual(passwordValidation(password), {
            "isValid": False,
            "errors": [
                "password must contain at least one capital letter"
            ]
        })

    def test_ShouldReturnAnError_WhenPasswordDoesNotContainASpecialCharacter(self):
        password = "Abcdef90"
        self.assertEqual(passwordValidation(password), {
            "isValid": False,
            "errors": [
                "password must contain at least one special character"
            ]
        })

    def test_ShouldReturnValidTrueAndEmptyErrors_WhenPasswordIsCorrect(self):
        password = "AlEt12$%"
        self.assertEqual(passwordValidation(password), {
            "isValid": True,
            "errors": []
        })

    def test_ShouldReturnMultipleErrors_WhenPasswordFailsMoreThanOneValidation(self):
        password = "abcdefg"
        self.assertEqual(passwordValidation(password), {
            "isValid": False,
            "errors": [
                "Pasword must be at least 8 characters",
                "The passwordd must contain at least 2 numbers",
                "password must contain at least one capital letter",
                "password must contain at least one special character"
            ]
        })