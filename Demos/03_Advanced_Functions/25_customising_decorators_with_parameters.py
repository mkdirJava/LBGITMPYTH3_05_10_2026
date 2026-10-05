def transaction_logger(label):  # 1. Outer: Catch the parameter
    def decorator(func):       # 2. Middle: Catch the function
        def wrapper(self, amount):
            print(f"[LOG] Starting {label} for {self.owner}...")
            result = func(self, amount)
            print(f"[LOG] {label} finished. Balance: ${self.balance}")
            return result
        return wrapper
    return decorator

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @transaction_logger("DEPOSIT") # Parameter "DEPOSIT" passed here
    def deposit(self, amount):
        self.balance += amount

    @transaction_logger("WITHDRAWAL") # Parameter "WITHDRAWAL" passed here
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("Ted", 1000)
account.deposit(100)
account.withdraw(75)
