from typing import Union, Dict

# Define a type alias for readability
DepositInput = Union[float, str, Dict[str, float]]
# OR
# DepositInput = float | str | dict[str, float]

# DepositInput = Union[int, str, Dict[str, float]]

def process_deposit(account_id: str, deposit: DepositInput) -> float:
    #Processes different types of deposits and returns the final amount credited.
    if isinstance(deposit, float):
        print(f"Cash deposit received: £{deposit}")
        return deposit
    elif isinstance(deposit, str):
        # Simulate lookup for cheque/reference
        print(f"Looking up deposit reference: {deposit}")
        resolved_amount = 250.00  # mock lookup result
        return resolved_amount
    elif isinstance(deposit, dict):
        # Expecting something like {"amount": 100.0}
        amount = deposit.get("amount", 0.0)
        print(f"Bank transfer received: £{amount}")
        return amount
    else:
        raise ValueError("Unsupported deposit type")

# Example usage
balance = 1000.0

balance += process_deposit("ACC123", 200.0)                 # cash
balance += process_deposit("ACC123", "CHK-987654")          # cheque reference
balance += process_deposit("ACC123", {"amount": 150.0})     # transfer

balance += process_deposit("ACC123", 34)    # bad data type

print(f"Updated balance: £{balance}")


