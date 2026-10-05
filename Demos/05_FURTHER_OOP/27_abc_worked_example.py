from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from the account"""
        pass

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print(f"{self.owner}: Overdraft limit exceeded")
        else:
            self.balance -= amount
            print(f"{self.owner}: Withdrew £{amount}")

class HighInterestAccount(Account):
    MIN_BALANCE = 10000.0
    def __init__(self, owner, balance=10000.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print(f"{self.owner}: Cannot go below £{self.MIN_BALANCE}")
        else:
            self.balance -= amount
            print(f"{self.owner}: Withdrew £{amount}")
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.owner}: Interest added £{interest:.2f}")


current = CurrentAccount("Peter", 100, overdraft_limit=50)
high_interest = HighInterestAccount("Alice", 15000, interest_rate=0.05)
current.withdraw(130)      # allowed (overdraft)
current.withdraw(50)       # exceeds overdraft
high_interest.withdraw(3000)   # blocked if it drops below 10,000
high_interest.apply_interest()

