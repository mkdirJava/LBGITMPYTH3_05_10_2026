from multiprocessing import Process
import time
import os
import random

def race_func(*args):
   print(args[0])
   sleep_duration = random.random() * 5
   print(f"{args[0]} sleeping for {round(sleep_duration, 2)} secs")
   time.sleep(sleep_duration)
   print(f"{args[0]} is awake!")
   print(f"parent process id: {os.getppid()}")
   print(f"process id: {os.getpid()}")
   time.sleep(2)

if __name__ == "__main__":
    race_func("exec from main")
    my_proc1 = Process(target=race_func, args=("1st func",))
    my_proc2 = Process(target=race_func, args=("2nd func",))
    my_proc1.start()
    my_proc2.start()
    my_proc1.join()
    my_proc2.join()
    print("Finished")
