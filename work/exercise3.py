from functools import wraps
from enum import Enum
from typing import Callable, List, Tuple
import re

def _check_sort_code(data: str) -> None:
    print("Checking sort code...")
    data = data.strip()
    if re.fullmatch(r"\d{2}-\d{2}-\d{2}", data) is None:
        raise ValueError("Invalid sort code!")

def _check_uk_account_number(data) -> None:
    print("Checking account number...")
    data = data.strip()
    if re.fullmatch(r"\d{8}", data) is None:
        raise ValueError("Invalid UK account number!")

def _check_payment_card_number(data: str):
    print("Checking card number...")
    data = data.strip()
    if re.fullmatch(r"[45]\d{15}", data) is None:
        raise ValueError("Invalid payment card number!")

class Action(Enum):
    check_sort_code = _check_sort_code
    check_uk_account_number = _check_uk_account_number
    check_payment_card_number = _check_payment_card_number

def validate_input(actions: List[Action]) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(input:str,*args, **kwargs):
            error_messages: List[str] = []
            for action in actions:
                try:
                    action(input)
                except ValueError as e:
                    error_messages.append(str(e))
            if len(error_messages) > 0:
                raise ValueError("".join(error_messages))
            return func(input,*args, **kwargs)

        return wrapper
    return decorator

@validate_input(actions = [Action.check_sort_code])
def make_payment(input: str )-> str:
    return input

def main():
    result = make_payment("00-00-00")
    print(result)   

if __name__ == "__main__":
    main()


