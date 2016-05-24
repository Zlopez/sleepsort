#!/usr/bin/python

import threading
import time
import random

class SleepSortThread(threading.Thread):
    def __init__(self, number,length):
        threading.Thread.__init__(self)
        self.number = number
        self.delay = (number*length/10)/1000

    def run(self): 
        #print("I will sleep for " + str(self.delay) + " seconds.")
        time.sleep(self.delay)
        print(str(self.number), end=" ", flush=True)

def createThreads(unsorted_list):
    thread_array = []
    for i in unsorted_list:
        thread_array.append(SleepSortThread(i, len(unsorted_array)))

    return thread_array

def startThreads(thread_array):
    for thread in thread_array:
        thread.start()

if __name__ == "__main__":
    #generate random unsorted array
    unsorted_array = []
    for i in range(0,random.randrange(1000)):
        unsorted_array.append(random.randrange(1000))

    print(unsorted_array)
    thread_array = createThreads(unsorted_array)
    startThreads(thread_array)

    while (threading.active_count() > 1):
        #print("Number of active threads: " + str(threading.active_count()))
        time.sleep(10/1000)

    print('\n')
