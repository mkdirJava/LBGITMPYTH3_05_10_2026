class Account:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency


# Create an account
acct = Account("Alice", 1000.0, "GBP")

# --- Using getattr ---
print("=== Using getattr ===")
# Safely access attributes dynamically
print("Owner:", getattr(acct, "owner"))
print("Balance:", getattr(acct, "balance"))

# Provide a default if attribute doesn't exist
credit_score = getattr(acct, "credit_score", "Not available")
print("Credit Score:", credit_score)


# --- Using setattr ---
print("\n=== Using setattr ===")
# Update balance dynamically (e.g., after a deposit)
setattr(acct, "balance", acct.balance + 250.0)
print("Updated Balance:", acct.balance)

# Add a new attribute dynamically (e.g., loan amount)
setattr(acct, "loan", 5000.0)
print("Loan Amount:", getattr(acct, "loan"))


# --- Realistic financial operation ---
print("\n=== Dynamic transaction processing ===")

transaction = {
    "type": "withdrawal",
    "amount": 200.0
}

# Use getattr to read, setattr to update
if transaction["type"] == "withdrawal":
    new_balance = getattr(acct, "balance") - transaction["amount"]
    setattr(acct, "balance", new_balance)

print("Balance after transaction:", acct.balance)




