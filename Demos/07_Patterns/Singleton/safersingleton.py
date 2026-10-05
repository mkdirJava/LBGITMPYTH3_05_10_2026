
class BankLedger:
    _instance = None

    # Must use __new__ and not __init__ because __init__ runs after an instance is already created.
    # To truly enforce a singleton, you must control instance creation, which is what __new__ does.
    def __new__(cls):
        if cls._instance is None:
            print("Creating the Bank Ledger instance...")
            cls._instance = super().__new__(cls)
            cls._instance.transactions = []
        return cls._instance

    def add_transaction(self, account_id, amount):
        self.transactions.append({
            "account_id": account_id,
            "amount": amount
        })

    def get_transactions(self):
        return self.transactions
