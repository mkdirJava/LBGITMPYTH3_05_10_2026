def log_action(func):
    """A decorator that logs the function call."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    # def wrapper(balance, amount):
    #     print(f"[LOG] Calling {func.__name__} with arguments {balance} {amount}")
    #     return func(balance, amount)
    # return wrapper
    # def wrapper(bal, amt):
    #     print(f"[LOG] Calling {func.__name__} with arguments {bal} {amt}")
    #     return func(bal, amt)
    # return wrapper

# Core banking function (un-decorated)
def deposit(balance, amount):
    return balance + amount

# --- Monkey patching the function with its decorated version ---
deposit = log_action(deposit)   # ← monkey patch

# Use it
balance = 100
balance = deposit(balance, 50) # two positional args and no keyword args
print("New balance:", balance)

balance = deposit(balance=balance, amount=50) # no positional args and two keyword args
print("New balance:", balance)

balance = deposit(balance, amount=50) # one positional arg and one keyword arg
print("New balance:", balance)

