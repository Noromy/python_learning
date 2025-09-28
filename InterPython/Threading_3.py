from threading import Thread, Lock, current_thread
from queue import Queue
import time



if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1
    first = q.get()
    print(first)

    # q.join() # Will excute after the main code has been executed and you can't countinue
    # q.task_done() # Telling that the q is done
    print ('end main')



def worker(q, lock):
    while True:
        value = q.get()
        time.sleep(0.01)
        #processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10 #thread compete for taking value so that the queue is random

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True # This will execute the func and will be false after finish 
        thread.start()

    for i in range(1, 21):
        q.put(i)

    
    q.join()

    print('end main')