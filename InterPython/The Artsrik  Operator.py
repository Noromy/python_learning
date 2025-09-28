result = 2 * 2
        # 2 ** 4 (Quadrat?Pangkat)
print(result)

zeros = [0, 1] * 10 # Times and element
        # "AB"
        # (0,1)
print(zeros)

def foo(a, b, *args, **kwargs): # You can see in file "Function Argument"
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)


def fool(a, b, *, c, d): # Parameter after * must be a keyword argument
    print(a, b, c, d)

 # fool(1, 2, 3, 4) Wrong
fool(1, 2, c=3, d=4)

# Unpacking Arguments
def fool(a, b, c): 
    print(a, b,c)


my_list = [2, 4, 5]
my_tuple = (0, 1, 2)
my_dict = {'a':1, 'b':2, 'c':3}
fool(*my_list)
fool(*my_tuple)
fool(*my_dict)
fool(**my_dict) # will print the value


# To make a single and multiple elements
number = [1, 2, 3, 4, 5, 6]

beginning, *middle, secondLast, last = number
# beginning, *last = number #  Unpack the last and remain the beginning
# beginning, *middle, last = number #  unpack all except the midlle (2, 3, 4)
# and so on
print(beginning)
print(last)
print(middle)


my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list] # Will make it into list
print(new_list)

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}

my_dict = {**dict_a, **dict_b} # Unpack Dictionary
print(my_dict)