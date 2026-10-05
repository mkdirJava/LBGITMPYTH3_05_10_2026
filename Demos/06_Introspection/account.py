class Account:
    def __init__(self, name="Anon", id="XXXXXXXX", initial_balance=0):
        self.__balance = initial_balance
        self.name = name
        self.id = id


    def deposit(self, amt):
        self.__balance += amt