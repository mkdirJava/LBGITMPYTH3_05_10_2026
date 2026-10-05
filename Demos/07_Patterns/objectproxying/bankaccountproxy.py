from account import Account
from bankaccount import BankAccount

class BankAccountProxy(Account):
    def __init__(self, bank_account: BankAccount):
        self._bank_account = bank_account

    def withdraw(self, amount: int) -> None:
        # Add custom behaviour
        if amount > 1000:
            print("Proxy: Large withdrawal flagged! Approval required.")
        else:
            self._bank_account.withdraw(amount)

    def __getattr__(self, name):
        """
        Delegate any missing attribute/method
        to the real account
        """
        print(f"Proxy forwarding '{name}'")
        return getattr(self._bank_account, name, "Anon")