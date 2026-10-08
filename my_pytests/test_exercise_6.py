import pytest
from work.play6 import CustomerProfileValidation

# --- Happy Path Test ---
def test_exercise_happy():
    customer_profile_validator = CustomerProfileValidation("h@gmail.com", "1234567890", "12345678")
    error_messages = customer_profile_validator.run_validations()
    
    # Standard pytest asserts use simple expressions
    assert len(error_messages) == 0

@pytest.mark.parametrize(
    "interested_scenario, expected_error_message",
    [
        (
            CustomerProfileValidation("hgmail.com", "1234567890", "12345678"), 
            "Email Validation failed"
        ),
        (
            CustomerProfileValidation("h@gmail.com", "123", "12345678"), 
            "Phone number number must be numeric and be 10 digits long"
        ),
        (
            CustomerProfileValidation("h@gmail.com", "1234567890", "123"), 
            "Customer id number number must be numeric and be 8 digits long"
        ),
    ]
)
def test_exercise_negative(interested_scenario: CustomerProfileValidation, expected_error_message: str):
    error_messages = interested_scenario.run_validations()
    
    assert len(error_messages) == 1
    assert expected_error_message in error_messages        