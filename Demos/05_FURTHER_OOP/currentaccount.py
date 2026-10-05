import account
class CurrentAccount(account.Account):

    def __init__(self, name, id,  initial, overdraft_limit):
        super().__init__(name, id, initial)
        # self._balance = initial
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amt):
        # check overdraft_limit
        if self._balance - amt < self._overdraft_limit:
            return
        self._balance -= amt
        return
