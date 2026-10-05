from functools import wraps
def security_audit(func):
    @wraps(func)  # Copies name and docstring
    def wrapper(self, *args, **kwargs):
        # Internal audit wrapper logic.
        print(f"Securing {func.__name__}...")
        return func(self, *args, **kwargs)
    return wrapper
class BankAccount:
    @security_audit
    def deposit(self, amount):
        """ increases funds after identity verification."""
        self.balance += amount
# Without @wraps: account.deposit.__name__ =>"wrapper"
# With @wraps:    account.deposit.__name__ is "deposit"
print(f"Function Name: {BankAccount.deposit.__name__}")
print(f"Docstring: {BankAccount.deposit.__doc__}")
