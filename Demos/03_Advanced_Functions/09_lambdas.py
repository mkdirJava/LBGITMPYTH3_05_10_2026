calculate_interest = lambda balance, rate: balance * rate

interest = calculate_interest(2000, 0.03)
print("Interest earned:", interest)


balances = [1200, 3400, 560, 890]

# Apply 2% monthly interest to each balance
updated_balances = list(map(lambda b: b * 1.02, balances))
print(updated_balances)

# Apply 5% monthly interest to each balance
updated_balances = [*map(lambda b: b * 1.05, balances)]
print(updated_balances)

print(*map(lambda b: b * 1.10, balances), sep=", ")


accounts = [
    ("Alice", 3200),
    ("Bob", 1500),
    ("Charlie", 5400),
    ("Diana", 2750)
]

# Sort accounts by balance
sorted_accounts = sorted(accounts, key=lambda account: account[1])

print(sorted_accounts)



def apply_fee(amount, fee):
    return amount - fee

transactions = [120, 85, 40]

# This fails
# map tries to call apply_fee(120), apply_fee(85), ...
#fees_applied = list(map(apply_fee(2), transactions))
# This works: lambda allows us to pass the extra parameter
#fees_applied = list(map(lambda t: apply_fee(t, 2), transactions))

#my_cubes = [x ** 3 for x in my_data]
fees_applied = [t - 2 for t in transactions]
print(fees_applied)