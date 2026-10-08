import unittest
from work.play6 import CustomerProfileValidation
from parameterized import parameterized

class Test_6(unittest.TestCase):
    def test_exercise_happy(self):
        customer_profile_validator = CustomerProfileValidation("h@gmail.com","1234567890","12345678")
        error_messages = customer_profile_validator.run_validations()
        self.assertTrue(len(error_messages) == 0)

    @parameterized.expand([
            [CustomerProfileValidation("hgmail.com","1234567890","12345678"), "Email Validation failed"],
            [CustomerProfileValidation("h@gmail.com","123","12345678"),"Phone number number must be numeric and be 10 digits long"],
            [CustomerProfileValidation("h@gmail.com","1234567890","123"),"Customer id number number must be numeric and be 8 digits long"],
        ])
    def test_exercise_negitive(self, intereted_scenario:CustomerProfileValidation, error_message: str ):
        error_messages = intereted_scenario.run_validations()
        self.assertTrue(len(error_messages) == 1)
        self.assertIn(error_message, error_messages)