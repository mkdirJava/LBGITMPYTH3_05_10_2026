from account import Account
class BankAccount(Account):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance = £{self.balance}")

