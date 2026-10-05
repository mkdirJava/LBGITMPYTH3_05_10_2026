def transfer_funds(balance, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
