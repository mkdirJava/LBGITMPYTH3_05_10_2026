from account2 import Account

acc = Account("Tina  Smith", "98127634", 2301.48)
print(acc.__slots__)

# Does my the Account class use slots?
if "__slots__" in Account.__dict__:
    print("slots:", acc.__slots__)
else:
    print("dict:", acc.__dict__)
