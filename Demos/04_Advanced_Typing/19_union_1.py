from typing import Union

my_union = Union[bool, int]
print(my_union)
print(type(my_union))

def is_prime_number(number: int) -> my_union:
    pass
print(help(is_prime_number))


