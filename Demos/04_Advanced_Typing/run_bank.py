# run_bank.py
from banking_monkeytype import process_deposit, get_transaction_type

# MonkeyType sees: str, float -> float
process_deposit("ACC-123", 250.50) 

# MonkeyType sees: int -> str
get_transaction_type(1) 