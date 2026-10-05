import random
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        time.sleep(random.random() * 5)
        print("From thread", self.name)
        time.sleep(5)

th1 = MyThread()
th2 = MyThread()
th1.start()
th2.start()
print("From main")
th1.join()
th2.join()

