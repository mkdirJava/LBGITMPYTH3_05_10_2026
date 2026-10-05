class Account:
    numCreated = 0


    def __init__(self, name="Anon", id="XXXXXXXX", initial_balance=0):
        self._balance = initial_balance
        self.name = name
        self.id = id
        Account.numCreated += 1


    def deposit(self, amt):
        self._balance += amt
        return


    def withdraw(self, amt):
        if self._balance - amt < 0:
            return
        self._balance -= amt
        return

    def setbalance(self, amt):
        if amt < 0:
            return
        self._balance = amt

    def getbalance(self):
        return self._balance

    def __str__(self):
        return f"Account {self.id} for {self.name} has a balance of £{self.balance}"

    balance = property(getbalance, setbalance)