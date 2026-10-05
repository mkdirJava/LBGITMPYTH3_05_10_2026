from collections import namedtuple
# Define the namedtuple type
account_fields = ["account_number", "customer_name", "balance"]
BankAccount = namedtuple("BankAccount", account_fields)
# Create account instances
acct1 = BankAccount(account_number="00123456", customer_name="Alice", balance=1500.00)
acct2 = BankAccount("00987654", "Bob", 320.75)
# see the schema (field names) of the namedtuple
print("BankAccount fields:", BankAccount._fields)



# turn a list of accounts into a list of plain dicts

accounts = [acct1, acct2]
# print("All accounts as list of BankAccounts:", accounts)

as_dicts = [a._asdict() for a in accounts]

print("All accounts as dicts:", as_dicts)
