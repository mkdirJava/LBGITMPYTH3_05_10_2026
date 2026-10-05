from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f"Account {self.account_number}, Balance: {self.balance:.2f}"

