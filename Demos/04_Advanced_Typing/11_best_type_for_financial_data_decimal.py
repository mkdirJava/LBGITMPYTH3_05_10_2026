# The trouble with floats
print(0.1 + 0.2)  # -> 0.30000000000000004

from decimal import Decimal
# price: Decimal = Decimal("101.2") # initial value will be 101.2 not a string

price: Decimal = Decimal("0.1") + Decimal("0.2")
print(price)
