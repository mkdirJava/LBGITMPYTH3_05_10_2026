from abc import *

class Account(ABC): # makes class a Metaclass which cannot be instantiated
    @abstractmethod
    def getType(self):
        pass

    def do_it(self):
        return "I'm doing it!"

class CurrentAccount(Account):
    def getType(self):
        print("CurrentAccount is an Account")

acc = CurrentAccount()
print(acc.getType())
print(acc.do_it())

# will error:
ac = Account()
print(ac.getType())
print(ac.do_it())

