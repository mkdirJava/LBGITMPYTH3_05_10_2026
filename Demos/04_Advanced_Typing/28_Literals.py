from typing import Literal, Union, TypedDict

# Define different structures for account types
class Savings(TypedDict):
    id: str
    bal: float
    rate: float

class Investment(TypedDict):
    id: str
    bal: float
    risk: Literal["Low", "Medium", "High"]


# Define a Union for the possible return types
AccountInfo = Union[Savings, Investment]

# A function that takes a Literal and returns a Union
def get_acc_details(
    id: str,
    type: Literal["SAVINGS", "INVESTMENT"]
) -> Union[AccountInfo, TypeError]:
    # Fetches account data based on the literal type provided.
    if type == "SAVINGS":
        return {"id": id, "bal": 1500.50, "rate": 0.02}
    elif type == "INVESTMENT":
        return {"id": id, "bal": 50000.00, "risk": "Medium"}
    else:
        raise TypeError(f"Invalid type {type}")

# Example usage
try:
    print(get_acc_details("SA-123", "SAVINGS"))
    print(get_acc_details("IA-456", "INVESTMENT"))
    print(get_acc_details("XX-000", "CHECKING")) # mypy error
except TypeError as e:
    print(f"Skipping invalid checking: {e}")

