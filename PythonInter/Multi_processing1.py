from multiprocessing import Process, Value, Array, Lock
import os
import time

from multiprocessing import Queue

def add_100(number, lock):
    for i in range(100):
       time.sleep(0.01)
       lock.acquire()
       number.value += 1
       lock.release()
        
        

if __name__ == '__main__': # Secure the excuse if it will be imported
    
    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at ending is ', shared_number.value)

def add_1001 (numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

if __name__ == '__main__': # Secure the excuse if it will be imported
    
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning is', shared_array[:]) #[:] this is for accessing all the elements

    p1 = Process(target=add_1001, args=(shared_array, lock))
    p2 = Process(target=add_1001, args=(shared_array, lock))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at ending is ', shared_array[:])


def Square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == '__main__': 
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=Square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    
    print('end main')

