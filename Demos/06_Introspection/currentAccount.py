import account
class CurrentAccount(account.Account):
    interest_rate = 0.01 # class attribute
    __secret_data = "secret"
    def __init__(self, name, id,  initial, overdraft_limit):
        super().__init__(name, id, initial)
        # self._balance = initial
        self._overdraft_limit = overdraft_limit # instance attribute (won't show when currentAccount.CurrentAccount.__dict__ is run)

    def withdraw(self, amt):
        # check overdraft_limit
        if self.__balance - amt < self._overdraft_limit:
            return
        self.__balance -= amt
        return
