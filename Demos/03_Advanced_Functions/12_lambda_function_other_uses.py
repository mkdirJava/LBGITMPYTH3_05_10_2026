def apply_fee(amount, fee):
    return amount - fee

transactions = [120, 85, 40]
# This fails
#fees_applied = list(map(apply_fee(2), transactions))

# Solved using a lambda
fees_applied = list(map(lambda t: apply_fee(t, 2), transactions))
print(fees_applied)

# better to have solved this with a list comprehension
fees_applied = [t - 2 for t in transactions]
print(fees_applied)

