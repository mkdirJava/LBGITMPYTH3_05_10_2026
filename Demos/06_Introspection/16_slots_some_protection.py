class Account:
    __slots__ = ['__name', '__id', '__balance']

    def __init__(self, name="Anon", id="XXXXXXXX", initial_balance=0):
        self.__balance = initial_balance
        self.__name = name
        self.__id = id

acc = Account("Brian May", "12345678", 1000.00)
# Attempt to create dynamic attribute
acc.email = "bmay.badger@stb.com"
