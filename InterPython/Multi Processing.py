from multiprocessing import Process
import os
import time

def square_number():
    for i in range(100):
        i * i  # atau bisa print(i * i) kalau mau lihat hasilnya
        time.sleep(0.1)
        

if __name__ == '__main__': # Secure the excuse if it will be imported
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine, usually a good choice for the number processes

    # create processes and asign a function for each process
    for i in range(num_processes):
        p = Process(target=square_number)
        processes.append(p)

    # start all process
    for p in processes:
        p.start()

    # wait for all processes ro finish
    # block  the main program until this processes are finished
    for p in processes:
        p.join()

    print('end main')