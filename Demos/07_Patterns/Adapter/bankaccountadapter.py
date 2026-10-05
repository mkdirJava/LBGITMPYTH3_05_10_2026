from abc import abstractmethod
from existing_incompatible_bankaccount_class import BankAccount

class CurrencyAdapter:
    @staticmethod
    @abstractmethod
    def convert(amount: float) -> float:
        pass

class PoundsToDollars(CurrencyAdapter):
    @staticmethod
    def convert(amount: float) -> float:
        return amount * 1.34 # conversion rate 28/05/2026

class PoundsToEuros(CurrencyAdapter):
    @staticmethod
    def convert(amount: float) -> float:
        return amount * 1.15 # conversion rate 28/05/2026

class BankAccountAdapter:
    def __init__(self, account: BankAccount, adaptee: CurrencyAdapter):
        self.account = account
        self.adaptee = adaptee

    def get_converted_balance(self):
        gbp = self.account.get_balance_gbp()
        converted_amount = self.adaptee.convert(gbp)
        return converted_amount
