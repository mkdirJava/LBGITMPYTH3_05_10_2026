
from sloppysingleton import SloppyBankLedger

ledger1 = SloppyBankLedger.get_ledger()
ledger2 = SloppyBankLedger.get_ledger()

ledger1.add_transaction("ACC123", 100)
ledger2.add_transaction("ACC345", -50)

print(ledger1.get_transactions())

# Issues
# You can still bypass it
another = SloppyBankLedger()  # completely separate instance!
another.add_transaction("ACC999", 99.99)

print(f"another: {another.get_transactions()}")
print(f"ledger1: {ledger1.get_transactions()}")
print(f"ledger2 (same as ledger1): {ledger1.get_transactions()}")

# Global state is exposed
_global_ledger = None  # someone can reset this accidentally!

# Not thread-safe. If twp threads run SloppyBankLedger.get_ledger() you may get two instances at the same time

# Hidden dependency
# Functions using SloppyBankLedger.get_ledger() rely on:
#
# implicit global state
# no clear dependency injection
