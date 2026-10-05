accounts = [
    ("Alice", 3200),
    ("Bob", 1500),
    ("Charlie", 5400),
    ("Diana", 2750)
]

# default (by initial entry alphabetically)
sorted_accounts = sorted(accounts)
print(sorted_accounts)

# Sort accounts by balance
sorted_accounts = sorted(accounts, key=lambda account: account[1])
print(sorted_accounts)

# default (by initial entry by string length)
sorted_accounts = sorted(accounts, key=lambda account: len(account[0]))
print(sorted_accounts)
