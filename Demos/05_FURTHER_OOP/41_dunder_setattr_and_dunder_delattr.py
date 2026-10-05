class BankAccount:
    def __init__(self, owner, balance):
        # Use super().__setattr__ to avoid recursion
        super().__setattr__('owner', owner)
        super().__setattr__('balance', balance)

    def __setattr__(self, name, value):
        print(f"[__setattr__] Attempting to set '{name}' to {value}")

        # Business rule: balance cannot go negative
        if name == "balance" and value < 0:
            raise ValueError("Balance cannot be negative!")

        # Business rule: owner name must be a string
        if name == "owner" and not isinstance(value, str):
            raise TypeError("Owner must be a string!")

        # Actually set the attribute
        super().__setattr__(name, value)
        print(f"[__setattr__] '{name}' successfully updated\n")

    def __delattr__(self, name):
        print(f"[__delattr__] Attempting to delete '{name}'")

        # Prevent deletion of critical financial data
        if name == "balance":
            raise AttributeError("Cannot delete balance from account!")

        super().__delattr__(name)
        print(f"[__delattr__] '{name}' deleted\n")


# --- Demonstration ---
acct = BankAccount("Alice", 1000)

print("\n--- Updating balance (valid) ---")
acct.balance = 1200

print("\n--- Attempting invalid balance update ---")
try:
    acct.balance = -500
except ValueError as e:
    print("Error:", e)

print("\n--- Updating owner ---")
acct.owner = "Bob"

print("\n--- Adding new attribute dynamically ---")
acct.currency = "GBP"

print("\n--- Deleting a non-critical attribute ---")
del acct.currency

print("\n--- Attempting to delete balance ---")
try:
    del acct.balance
except AttributeError as e:
    print("Error:", e)
