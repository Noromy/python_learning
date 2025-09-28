# The easier way
with open ('notes.txt', 'w') as file:
    file.write('Hidup jokowi...')
# The other way to open data
file = open('notes.txt', 'w')
try:
    file.write('Hidup jokowi...')
finally:
    file.close() # you have to put a close() statement



# The easier way to lock
from threading import Lock
lock = Lock()
# with lock:
#.....

# The other way

#lock.acquire()
#....
#lock.release()

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled') # This wil continue even the func has a ValueError if dont this wont print Continuing
       #  print('exc:', exc_type, exc_value)Checking Error
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('Selamat Pagi')
    file.write('Hidupp Jokowii....')
    file.somemethod()
print('countinuing')


from contextlib import contextmanager
@contextmanager
def open_manage_file(filename):

    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_manage_file('notes.txt') as f:
    f.write('Hidup Jokowii.....')
