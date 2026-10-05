from account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}")
        else:
            print("Overdraft limit exceeded")


