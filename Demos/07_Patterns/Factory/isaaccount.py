from account import Account

class ISAAccount(Account):
    def __init__(self, account_number, balance=0.0, max_balance=20000.0):
        super().__init__(account_number, balance)
        self.max_balance = max_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return

        if self.balance + amount <= self.max_balance:
            self.balance += amount
            print(f"Deposited {amount:.2f}")
        else:
            print("Deposit would exceed ISA limit")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}")
        else:
            print("Insufficient funds")


