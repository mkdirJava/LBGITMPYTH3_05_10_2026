class Thing():
    name: str = "unknown"
    def __init__(self, age: int):
        self.age = age
    def instance_method(self):
        print(self.name)
        print(self.age)
    @classmethod
    def class_method(cls)-> None:
        print(cls.name)
    @staticmethod
    def static_method()-> None:
        print("I am static")
        
# t = Thing(2)
# t.instance_method()
# t.class_method()
# t.static_method()


# class Thing_2(Thing):

#     def __init__(self, age):
#         super().__init__(age)

#     def instance_method(self):
#         print("i am in the child")


# t = Thing_2(2)
# t.instance_method()


from collections.abc import Iterable, Iterator

class TransactionIterator(Iterator[float]):
    """Explicitly states it is an Iterator that yields float values."""
    
    def __init__(self, transactions: list[float]) -> None:
        self._transactions: list[float] = transactions
        self._index: int = 0

    def __iter__(self) -> Iterator[float]:
        return self

    def __next__(self) -> float:
        if self._index >= len(self._transactions):
            raise StopIteration
        value: float = self._transactions[self._index]
        self._index += 1
        return value

class BankAccount(Iterable[float]):
    """Explicitly states it is an Iterable containing float elements."""
    
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.transactions: list[float] = []

    def add_transaction(self, amount: float) -> None:
        self.transactions.append(amount)

    def __iter__(self) -> Iterator[float]:
        return TransactionIterator(self.transactions)
    
    # sort collections @total_ordering, plus __eq__ and __lt__ gives sorted()
    # You can also do this with a lambda
    # property looks very interesting 
