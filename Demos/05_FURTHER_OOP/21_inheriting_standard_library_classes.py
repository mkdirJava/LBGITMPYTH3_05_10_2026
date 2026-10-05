from collections import namedtuple

# Base namedtuple
BankAccount = namedtuple("BankAccount", ["owner", "balance"])


# Extend namedtuple with methods
class SavingsAccount(BankAccount):

    def deposit(self, amount):
        return self._replace(balance=self.balance + amount) # tuples are immutable so replace rather than amend

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        return self._replace(balance=self.balance - amount)


# Create account
account = SavingsAccount("Alice", 1000)

print("Original:", account)

# Deposit money
account = account.deposit(500)
print("After deposit:", account)

# Withdraw money
account = account.withdraw(300)
print("After withdrawal:", account)