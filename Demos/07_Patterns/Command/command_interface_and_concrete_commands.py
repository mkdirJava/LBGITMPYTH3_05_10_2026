# Command
from abc import abstractmethod
class Command:
    @abstractmethod
    def execute(self):
        pass


# Concrete Commands
class DepositCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)

class WithdrawCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)
