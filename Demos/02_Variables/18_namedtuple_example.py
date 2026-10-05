from collections import namedtuple
# Define the namedtuple type
account_fields = ["account_number", "customer_name", "balance"]
BankAccount = namedtuple("BankAccount", account_fields)
# Create account instances
acct1 = BankAccount(account_number="00123456", customer_name="Alice", balance=1500.00)
acct2 = BankAccount("00987654", "Bob", 320.75) # can be done positionally
# Accessing fields
print(f"{acct1.customer_name} has £{acct1.balance}")
print(f"Account {acct2.account_number} belongs to {acct2.customer_name}")
# Updating a balance using _replace (namedtuples are immutable)
acct1_updated = acct1._replace(balance=acct1.balance + 200)
print(f"After deposit: {acct1_updated.customer_name} now has £{acct1_updated.balance}")
