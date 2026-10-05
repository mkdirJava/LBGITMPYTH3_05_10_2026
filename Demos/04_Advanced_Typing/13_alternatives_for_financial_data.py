# Use local alias for Decimal
from decimal import Decimal as D
price: D = D("101.2")
tax_rate: D = D("102.50")

# Use factory function
from decimal import Decimal
def money(value: str) -> Decimal:
    return Decimal(value)

price = money("101.2")

from typing import Annotated
Pence = Annotated[int, "amount in pence"]
balance: Pence = 1299  # £12.99


