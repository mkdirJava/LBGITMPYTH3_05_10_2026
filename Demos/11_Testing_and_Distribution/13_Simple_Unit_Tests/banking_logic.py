def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    return balance + amount

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount