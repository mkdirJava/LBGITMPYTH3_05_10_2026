from collections import defaultdict

# Incoming transactions across many accounts
transactions = [("ACC1001", 500.00),("ACC1002", 125.00),("ACC1001", -75.00),
("ACC1003", 300.00),("ACC1002", -25.00),("ACC1001", 50.00),]
# Start each unseen account at 0.0 automatically
balances = defaultdict(float)

for account_id, amount in transactions:
    balances[account_id] += amount
# Accessing a missing account safely returns 0.0 (and creates the key)
print("ACC9999 balance:", balances["ACC9999"])
# Report balances
for acc, bal in balances.items():
    print(f"{acc}: £{bal:.2f}")
