class Account:
    def __init__(self):
        self.__balance = ""

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance must be positive")
        self.__balance = new_balance

account = Account()
account.balance = 101.56
print(account.balance)






