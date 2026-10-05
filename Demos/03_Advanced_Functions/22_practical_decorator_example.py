# Pie Syntax Decorator:
def limit_withdrawals(func):
    """Decorator enforcing a max withdrawal amount per transaction."""
    def wrapper(balance, amount):
        if amount > 300:
            raise ValueError("Withdrawal exceeds daily limit of £300.")
        print(f"[SECURITY] Withdrawal validated: £{amount}")
        return func(balance, amount)
    return wrapper

@limit_withdrawals   # ← pie syntax decorating the function
def withdraw(balance, amount):
    return balance - amount

# Use it
balance = 500
balance = withdraw(balance, 100)
print("New balance:", balance)

balance = withdraw(balance=balance, amount=100)
print("New balance:", balance)
