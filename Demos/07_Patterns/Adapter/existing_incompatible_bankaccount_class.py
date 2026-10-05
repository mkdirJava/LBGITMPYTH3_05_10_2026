class BankAccount:
    def __init__(self, owner, balance_gbp: float):
        self.owner = owner
        self.balance_gbp = balance_gbp

    def get_balance_gbp(self) -> float:
        return self.balance_gbp

# Problem
# A new service expects: get_balance_usd()
# but we don't want to change original code in this class