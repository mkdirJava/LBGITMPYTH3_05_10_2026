def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def check_balance(balance, *_):
    return balance

# Dispatch table mapping operation names to functions
operations = {
    "deposit": deposit,
    "withdraw": withdraw,
    "check_balance": check_balance
}

def process_trans(balance, op, amount=0):
    try:
        action = operations[op]
    except KeyError:
        raise ValueError(f"Unknown operation: {op}")

    return action(balance, amount)

bal = 100
bal = process_trans(bal, "deposit", 50)
bal = process_trans(bal, "withdraw", 20)
bal = process_trans(bal, "check_balance")

print(bal)
