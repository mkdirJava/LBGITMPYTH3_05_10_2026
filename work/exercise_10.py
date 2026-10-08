from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Manager
from multiprocessing.managers import DictProxy
import time
from typing import List

class PlayThreadExecutor():

    def __init__(self):
        self.thread_pool_executor:ThreadPoolExecutor = ThreadPoolExecutor()
        self.result = self.thread_pool_executor.submit(lambda : print("I am a piece of work"))

    def do_it(self):
        while True:
            if self.future_result.done():
                result = self.future_result.result(1)
                print("I am done")
                break
            time.sleep(0.01)

from concurrent.futures import Future, ProcessPoolExecutor, as_completed
import time

class PlayProcessExecutor():

    def __init__(self):
        self.executor = ProcessPoolExecutor()

    @staticmethod
    def action(message: str)-> str:
        return f"This is a greeting {message}"
    
    def do_something(self) -> str:
        result_future = self.executor.submit(PlayProcessExecutor.action,"Bob")
        return result_future.result(1)
    
    @staticmethod
    def action_shared(results: DictProxy):
        results["done"] ="done"


    def do_somthing_shared(self) -> DictProxy:
        manager = Manager()
        shared_dictionary = manager.dict()
        result_future = self.executor.submit(PlayProcessExecutor.action_shared,shared_dictionary)
        while( result_future.done() is False):
            time.sleep(1)
        return shared_dictionary

from datetime import datetime
import threading 
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import threading
from typing import List

class TransactionNumberParallel:

    def __init__(self, worker_count: int, prefix: str):
        self.thread_executor = ThreadPoolExecutor(max_workers=worker_count)
        self.prefix: str = prefix
        self.time_lock = threading.Lock()
        self.counter = 0

    @staticmethod
    def _padding_counter(counter: int) -> str:
        counter_string = str(counter)
        padding_size = 4 - len(counter_string)
        padding_size = max(0, padding_size) 
        return f"{'0' * padding_size}{counter_string}"
    
    def _get_time(self) -> str:
        with self.time_lock:
            date = datetime.today()
            formatted_time = date.strftime("%Y-%m-%d %H:%M:%S")
            transaction_time = f"{formatted_time}-{self._padding_counter(self.counter)}"
            self.counter += 1
            return transaction_time
            
    def _create_transaction(self) -> str:
        return f"{self.prefix}-{self._get_time()}"

    def get_transactions(self) -> List[str]:
        futures = []
        # Submit all tasks concurrently
        for _ in range(40):
            futures.append(self.thread_executor.submit(self._create_transaction))
        
        # Gather results
        return [f.result() for f in futures]

