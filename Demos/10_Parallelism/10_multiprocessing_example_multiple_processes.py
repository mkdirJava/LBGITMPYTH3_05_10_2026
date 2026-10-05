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
    my_processes = []
    race_func("exec from main")
    for i in range(2):
        temp_proc = Process(target=race_func, args=(f"process {i}",))
        temp_proc.start()
        my_processes.append(temp_proc)
    for each_process in my_processes:
        each_process.join()
    print("Finished")
