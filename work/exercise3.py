from  functools import wraps


def _check_sort_code():
    pass
def _check_uk_account_number():
    pass
def _check_payment_card_number():
    pass

def validate_input(func):
    @wraps(func)
    def wrapper(input:str,*args, **kwargs):
        # print(input)
        # _check_payment_card_number()
        _check_sort_code(input)
        return func(input,*args, **kwargs)
    return wrapper



@validate_input
def make_payment(input: str)-> str:
    return input
result = make_payment("hi")
print(result)



# from functools import wraps

# def _check_sort_code(val: str):
#     print("Checking sort code...")

# def _check_uk_account_number(val: str):
#     print("Checking account number...")

# def _check_payment_card_number(val: str):
#     print("Checking card number...")

# def validate_input(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         return func(*args, **kwargs)
#     return wrapper

# @validate_input
# def make_payment(input: str) -> str:
#     return f"Payment processed for: {input}"

# print(make_payment("hi"))