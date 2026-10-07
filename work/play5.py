
    
from datetime import datetime
from typing import Iterable, Iterator

class BankAccountTransactionIterator(Iterable[str]):
    """Explicitly states it is an Iterable containing float elements."""
    
    def __init__(self, prefix: str) -> None:
        self.prefix: str = prefix
        self.transactions: list[float] = []
        self.counter = 0

    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        last_time = None
        if last_time is not None and last_time == self._get_time():
            self.counter = 0  
        last_time = self._get_time()
        try:
            return f"{self.prefix}-{last_time}-{self._padding_coutner(self.counter)}"
        finally:
            self.counter = self.counter + 1

    def _get_time(self) -> str:
        date = datetime.today()
        date.strftime
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def _padding_coutner(self,counter: int)-> str:
        counter_string = str(counter)
        counter_string_len = len(counter_string)
        padding_size = 4 - counter_string_len
        return f"{padding_size * '0'}{counter}"

        
bankTransderAccountTransactionIterator = BankAccountTransactionIterator("transaction")
import time

for _ in range(21):
    print(next(bankTransderAccountTransactionIterator))
    time.sleep(0.1)