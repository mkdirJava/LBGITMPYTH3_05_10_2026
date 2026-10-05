# In Python, a “typing comparison” usually refers to comparing type hints
# (from the typing module or built‑in generics) to check whether two types are:
# - equal
# - compatible
# - subtypes
# - assignable
#
# This shows up when writing type‑aware logic, such as validators, data pipelines,
# serializers, API layers, or frameworks.

#1. Comparing type hints for equality
# You can compare type hints directly:
from typing import List, Dict
print(List[int] == List[int])     # True
print(List[int] == List[str])     # False
print(Dict[str, int] == Dict[str, int])  # True
# Useful for writing a type‑driven serializer, field validator, or schema engine.


# 2. Comparing runtime types with generics (PEP 585)
# Modern Python allows built‑in generics:
list[int] == list[int]      # True
list[int] == list[str]      # False
# This is often used in data‑validation logic.


# 3. Comparing the origin and arguments of a type
# When comparing complex types like list[int] or dict[str, float], you often use:
# - get_origin() → the base type (e.g., list)
# - get_args() → inner types (e.g., (int,))
#
from typing import get_origin, get_args, List
T = List[int]
print(get_origin(T))     # <class 'list'>
print(get_args(T))       # (int,)
# You can then compare these parts:
def same_type(t1, t2):
    return get_origin(t1) == get_origin(t2) and get_args(t1) == get_args(t2)
print(same_type(List[int], list[int]))  # True
print(same_type(List[int], List[str]))  # False


# 4. Checking subtype relationships
# Typing also allows you to test whether one type is a subtype (i.e., assignable to another).
# Example using typing.TypeGuard or custom logic:
from typing import Iterable

def is_iterable(tp):
    return issubclass(tp, Iterable)

print(is_iterable(list))  # True
print(is_iterable(int))   # False

# Or with generic introspection:
from typing import Sequence
print(issubclass(list, Sequence))   # True
print(issubclass(tuple, Sequence))  # True
# Used heavily in schema engines and ETL pipelines.


# 5. Comparing against Any, Union, and Optional
# These require special comparison rules:
from typing import Any, Union, Optional, get_args
print(Any == Any)  # True
print(Union[int, str] == Union[str, int])   # True (order doesn’t matter)
print(Optional[int] == Union[int, type(None)])  # True


#  Putting it together: financial example
# This example validates fields in a financial data schema using typing comparisons.
from typing import List, Dict, get_origin, get_args
schema = {    "prices": List[float],    "volumes": List[int],    "meta": Dict[str, str]}
data = {    "prices": [101.2, 102.5, 103.1],    "volumes": [100, 200, 150],    "meta": {"source": "Bloomberg"}}
def validate(expected, value):
    origin = get_origin(expected)
    args = get_args(expected)
    if origin is list:
        return all(isinstance(v, args[0]) for v in value)
    if origin is dict:
        return (all(isinstance(k, args[0]) for k in value.keys()) and
                all(isinstance(v, args[1]) for v in value.values()))
    return isinstance(value, expected)

for field, typ in schema.items():
    print(field, "valid:", validate(typ, data[field]))
# This uses type comparisons to enforce a financial schema.



from decimal import Decimal

def calculate_total(price: Decimal, tax_rate: Decimal) -> Decimal:
    return price * (1 + tax_rate)

# The trouble with floats
print(0.1 + 0.2)  # -> 0.30000000000000004


price: Decimal = Decimal("101.2")
tax_rate: Decimal = Decimal("102.50")


from typing import Annotated

Pence = Annotated[int, "amount in pence"]
balance: Pence = 1299  # £12.99

from decimal import Decimal as D

price: Decimal = D("101.2")
tax_rate: Decimal = D("102.50")

Money = Decimal


def money(value: str) -> Money:
    return Decimal(value)

price = money("101.2")
