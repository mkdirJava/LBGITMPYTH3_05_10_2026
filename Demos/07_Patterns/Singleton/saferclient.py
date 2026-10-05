from safersingleton import BankLedger

ledger1 = BankLedger()
ledger2 = BankLedger()

ledger1.add_transaction("ACC123", 500)
ledger2.add_transaction("ACC456", -200) # Won't create a new instance so parameters ignored

print(ledger1.get_transactions())


