from collections.abc import Generator
from datetime import datetime
from typing import List
import time

def _get_time() -> str:
    date = datetime.today()
    date.strftime
    return date.strftime("%Y-%m-%d %H:%M:%S")

def _padding_coutner(counter: int)-> str:
    counter_string = str(counter)
    counter_string_len = len(counter_string)
    padding_size = 4 - counter_string_len
    return f"{padding_size * '0'}{counter}"


def transaction_refrence_generator(prefix:str ="transactions") -> Generator[str, None, None]:
    counter:int = 0
    last_time = None
    while True:
        if last_time is not None and last_time == _get_time():
            counter =0 
        last_time = _get_time()
        yield  f"{prefix}-{last_time}-{_padding_coutner(counter)}"
        counter = counter + 1

transaction_generator = transaction_refrence_generator()
results: List[str] = []
for unit in range(0,20):
    next_value = next(transaction_generator)
    print(next_value)
    results.append(next_value)
    time.sleep(0.1)
print(results)