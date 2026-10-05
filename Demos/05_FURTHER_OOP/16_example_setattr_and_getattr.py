class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# --- Usage ---
account = BankAccount("Alice", 1000)

updates = {
    "balance": 1500,
    "overdraft_limit": 200
} # Could come from file or API stream

for key, value in updates.items():
    current_value = getattr(account, key, None)  # get existing value (if any)
    print(f"Updating '{key}': {current_value} -> {value}")

    setattr(account, key, value)

# From PowerPoint Notes Page
attributes = {
    "owner",
    "balance",
    "overdraft_limit",
    "account_type"
}

for key in attributes:
    current_value = getattr(account, key, None)  # get existing value (if any)
    print(f"Current attributes: '{key}': {current_value}")
