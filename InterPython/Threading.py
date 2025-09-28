
from threading import Thread
import os
import time

def square_number():
    for i in range(100):
        i * i  # atau bisa print(i * i) kalau mau lihat hasilnya
        time.sleep(0.1)
        

if __name__ == '__main__': # Secure the excuse if it will be imported
    threads = []
    num_threads = 10
    # create processes
    for i in range(num_threads):
        t = Thread(target=square_number)
        threads.append(t)

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()

    print('end main')