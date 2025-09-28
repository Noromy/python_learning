 #@mydecorator
#dosomething():

import functools


def start_end_decorator(func): #func = print_name
  
    def wrapper():
        print("start")
        func()
        print("End")
    return wrapper

@start_end_decorator #print_name = start_end_decorator(print_name)
def print_name():
    print("Imron")

print_name()


def start_end_decorator(func):
    @functools.wraps(func) # to preserve the original function's metadata  #print(help(add))
    #print(add.__name__)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print(result)
        print("End")
        return result
        
    return wrapper

@start_end_decorator
def add(x):
    return x + 5

result = add(10)
print(result)

