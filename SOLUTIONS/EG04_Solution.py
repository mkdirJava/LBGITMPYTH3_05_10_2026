#from __future__ import annotations

import re
from functools import wraps
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[[str], bool])


def validate_input(func: F) -> F:
    """
    Ensure the provided input is a string before calling the wrapped function.

    The wrapped function is responsible for domain-specific validation.
    """

    @wraps(func)
    def wrapper(data: object) -> bool:
        if not isinstance(data, str):
            raise TypeError("Your input must be a string")
        return func(data)

    return cast(F, wrapper)


@validate_input
def check_sort_code(data: str) -> bool:
    """
    Validate that a UK sort code matches the format NN-NN-NN.

    Leading/trailing whitespace is ignored.
    """
    data = data.strip()

    if re.fullmatch(r"\d{2}-\d{2}-\d{2}", data) is None:
        raise ValueError(
            "Invalid sort code. Expected format: 2digits-2digits-2digits."
        )
    return True


@validate_input
def check_uk_account_number(data: str) -> bool:
    """
    Validate that a UK account number consists of exactly 8 digits.

    Leading/trailing whitespace is ignored.
    """
    data = data.strip()

    if re.fullmatch(r"\d{8}", data) is None:
        raise ValueError("Invalid UK account number. Expected exactly 8 digits.")
    return True


@validate_input
def check_payment_card_number(data: str) -> bool:
    """
    Validate that a payment card number is 16 digits long and starts with 4 or 5.

    Leading/trailing whitespace is ignored.
    """
    data = data.strip()

    if re.fullmatch(r"[45]\d{15}", data) is None:
        raise ValueError(
            "Invalid payment card number. Expected 16 digits starting with 4 or 5."
        )
    return True


if __name__ == "__main__":
    examples: list[tuple[str, Callable[[str], bool], str]] = [
        ("Sort code", check_sort_code, " 12-34-56 "),
        ("UK account number", check_uk_account_number, " 12345678 "),
        ("Payment card number", check_payment_card_number, " 4123456789012345 "),
    ]

    for label, function, value in examples:
        print(f"{label}: {function(value)}")

    invalid_examples: list[tuple[Callable[[Any], bool], Any]] = [
        (check_sort_code, 123456),
        (check_sort_code, " 123456 "),
        (check_uk_account_number, " 1234 "),
        (check_payment_card_number, " 6123456789012345 "),
    ]

    for function, value in invalid_examples:
        try:
            function(value)
        except (TypeError, ValueError) as exc:
            print(f"{function.__name__}({value!r}) failed: {exc}")