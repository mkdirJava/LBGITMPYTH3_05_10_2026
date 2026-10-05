class TransactionLoggingMixin:
    def log_transaction(self, message):
        print(f"[LOG] {message}")


class FeeMixin:
    def apply_fee(self, amount):
        fee = amount * 0.02
        self.balance -= fee
        self.log_transaction(f"Fee applied: £{fee:0.00}")

class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class PremiumAccount(TransactionLoggingMixin, FeeMixin, BankAccount): # multiple inheritance
    def withdraw(self, amount):
        if amount > self.balance:
            self.log_transaction(f"{self.owner} failed withdrawal")
        else:
            self.balance -= amount
            self.log_transaction(f"{self.owner} withdrew £{amount}")
            self.apply_fee(amount)

acct = PremiumAccount("Peter", 100)

acct.deposit(50)
acct.withdraw(100)
