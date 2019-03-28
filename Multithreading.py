#Global interpretor lock prevent the threads running in parallel in python and can use one processor at a time
# Python use thread/task switching to perfrom multithreading and it executes rapidly that seems like task are running in parallel
# They are not running multiple task in parallel it seems like
import threading
import time
# In order to initiate a thread we need a function
def sleeper(n,name):
    print("Hi , I am {}, going to sleep for 5 seconds\n".format(name))
    time.sleep(n)
    print("{} has woken up from sleep \n".format(name))
sleeper(5,"ankit")

#initialize a thread
t=threading.Thread(target=sleeper,name="thread1",args=(10,"thread1"))   
t.start()
print("\nThread")
print("Thread")
print(help("threading"))
print(help("self"))
import math
print(math.sqrt(12.5))
def sum():

    

