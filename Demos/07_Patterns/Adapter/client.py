from existing_incompatible_bankaccount_class import BankAccount
from bankaccountadapter import BankAccountAdapter
from bankaccountadapter import PoundsToDollars
from bankaccountadapter import PoundsToEuros

account = BankAccount("Peter", 1000.00)

# Wrap it with adapter
adapted_account = BankAccountAdapter(account, PoundsToDollars)
print(f"Balance in USD: ${adapted_account.get_converted_balance()}")

adapted_account = BankAccountAdapter(account, PoundsToEuros)
print(f"Balance in Euros: \u20AC{adapted_account.get_converted_balance()}")