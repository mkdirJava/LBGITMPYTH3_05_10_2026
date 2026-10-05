from account import Account
from currentaccount import CurrentAccount

some_account = Account("Ted", "12345678", 1000.00)
another_account = Account("Mary", "12345679", 2000.00)
some_account.deposit(550.23)
some_account.deposit(100)
some_account.withdraw(50)
# some_account._balance = -800

some_account.balance = 34

some_account.balance = -50

print(some_account.balance)
print(Account.numCreated)

# my_current_account = CurrentAccount("Ted Bovis", "1212121212", 100, 200)
# my_current_account.deposit(50)
# print(my_current_account.balance)
# my_current_account.withdraw(350)

acc = CurrentAccount("Sadia Patel", '79927398718', 200.00, 500.00)

if isinstance(acc, CurrentAccount):
    print(acc, "is a CurrentAccount!")

if isinstance(acc, Account):
    print(acc, "is an Account!")

if issubclass(CurrentAccount, Account):
    print("CurrentAccount is a subclass of Account")
