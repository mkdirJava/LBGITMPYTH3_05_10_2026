from pprint import pprint
from currentAccount import CurrentAccount
from account import Account

pprint(Account.__dict__)
print("**************************************")
pprint(CurrentAccount.__dict__)
print("**************************************")
acc = CurrentAccount("Tina  Smith", "98127634", 2301.48, 500.00)
pprint(acc.__dict__)
acc.deposit(100)
print("**************************************")
pprint(acc.__dict__)