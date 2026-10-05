import random
from threading import Thread, Lock
import time

lock_stdout = Lock()

def myfunc(*args):
    lock_stdout.acquire()
    time.sleep(random.random() * 5)
    print(f"From thread {args[0]}")
    lock_stdout.release()

th1 = Thread(target=myfunc, args='1')
th2 = Thread(target=myfunc, args='2')
th1.start()
th2.start()
lock_stdout.acquire()
print("From main")
lock_stdout.release()
th1.join()
th2.join()
