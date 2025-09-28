import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4) # using num_times=.. to be clear and self documenting (easy to be read by anyone)
def greet(name):
    print(f"Hello {name}")
greet("Imron")


def start_end_decoderator(func):
     @functools.wraps(func)
     def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print(result)
        print("End")
        return result
     return wrapper

def debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")           # 4
        return result
    return wrapper


@debugger
@start_end_decoderator
def say_hello(name):
    greeting = f"Hello {name}"
    return greeting

say_hello("Imron")