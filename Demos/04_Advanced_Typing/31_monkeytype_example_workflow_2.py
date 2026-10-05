# banking.py after running monkeytype apply banking
def process_deposit(account_id: str, amount: float) -> float:
    """Update balance and return the new total."""
    # Simulated database lookup
    current_balance = 1000.0
    new_balance = current_balance + amount
    return new_balance

def get_transaction_type(code: int) -> str:
    """Convert a numeric code to a string label."""
    mapping = {1: "CREDIT", 2: "DEBIT"}
    return mapping.get(code, "UNKNOWN")


