class Account:
    def __init__(self):
        self.__balance = ""

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance must be positive")
        self.__balance = new_balance

    balance = property(get_balance, set_balance)

account = Account()
account.balance = 101.56
print(account.balance)
