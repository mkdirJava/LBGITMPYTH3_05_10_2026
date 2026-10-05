class Account():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

def print_account(account):
    print(account.balance)

x = Account(1200)
if hasattr(x, "deposit") and callable(x.deposit):
    print("x.deposit exists and is callable")
if hasattr(x, "myfunc") and callable(x.myfunc):
    print("x.myfunc exists and is callable")

if "print_account" in locals() and callable(print_account):
    print("local function 'print_account' exists and is callable")
if "myfunc" in locals() and callable(myfunc):
    print("local function 'myfunc' exists and is callable")


try:
    withdraw(100)
except NameError as err:
    print("'withdraw' function is not available")
