import random
from threading import Thread
import time

def myfunc(*args):
    time.sleep(random.random() * 5)
    print(f"From thread {args[0]}")

th1 = Thread(target=myfunc, args='1')
th2 = Thread(target=myfunc, args='2')
th1.start()
th2.start()
print("From main")
th1.join()
th2.join()
