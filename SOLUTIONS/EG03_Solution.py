from functools import wraps
import re


def validate_input(func):
    @wraps(func)
    def wrapper(data):
        if not isinstance(data, str):
            raise TypeError("Your input must be a string")
        return func(data)
    return wrapper


@validate_input
def check_sort_code(data):
    data = data.strip()
    if re.fullmatch(r"\d{2}-\d{2}-\d{2}", data) is None:
        raise ValueError("Invalid sort code!")
    return True


@validate_input
def check_uk_account_number(data):
    data = data.strip()
    if re.fullmatch(r"\d{8}", data) is None:
        raise ValueError("Invalid UK account number!")
    return True


@validate_input
def check_payment_card_number(data):
    data = data.strip()
    if re.fullmatch(r"[45]\d{15}", data) is None:
        raise ValueError("Invalid payment card number!")
    return True


if __name__ == "__main__":
    # Valid
    print(check_sort_code(" 12-34-56 "))
    print(check_uk_account_number(" 12345678 "))
    print(check_payment_card_number(" 4123456789012345 "))

    # Invalid - different technique (to shorten)
    for fn, value in [
        (check_sort_code, 123456),
        (check_sort_code, " 123456 "),
        (check_uk_account_number, " 1234 "),
        (check_payment_card_number, " 6123456789012345 "),
    ]:
        try:
            print(fn(value))
        except Exception as e:
            print(e)