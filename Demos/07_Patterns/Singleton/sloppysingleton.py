_global_ledger = None  # module-level variable! Not good

class SloppyBankLedger:
    _global_ledger = None

    def __init__(self):
        self.transactions = []

    def add_transaction(self, account_id, amount):
        self.transactions.append({
            "account_id": account_id,
            "amount": amount
        })

    def get_transactions(self):
        return self.transactions

    @staticmethod
    def get_ledger():
        global _global_ledger

        if _global_ledger is None:
            print("Creating sloppy global ledger...")
            _global_ledger = SloppyBankLedger()

        return _global_ledger