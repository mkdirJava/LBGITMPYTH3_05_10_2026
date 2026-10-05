class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# --- Usage ---
account = BankAccount("Alice", 1000)

# Dynamically update attributes
setattr(account, "balance", 1200)
setattr(account, "account_type", "Savings")  # attribute didn't exist before

print(account.owner)         # Alice
print(account.balance)       # 1200
print(account.account_type)  # Savings

# Obviously we could have done the following:
account.owner = "Anna"
account.balance = 1300
account.account_type = "Current"
account.phone = "01273700966"

print(account.owner)         # Anna
print(account.balance)       # 1300
print(account.account_type)  # Current
print(account.phone)         # 01273700966

updates = {
    "balance": 1500,
    "overdraft_limit": 200
} # Could come from file or API stream

for key, value in updates.items():
    current_value = getattr(account, key, None)  # get existing value (if any)
    print(f"Updating '{key}': {current_value} -> {value}")

    setattr(account, key, value)

attributes = {
    "owner",
    "balance",
    "overdraft_limit",
    "account_type"
}
for key in attributes:
    current_value = getattr(account, key, None)  # get existing value (if any)
    print(f"Current attributes: '{key}': {current_value}")


