def print_name(name): #Parameter
    print(name)

print_name("Alex")  #Argument

def fool(a, b, c):
    print(a, b, c)

fool(1, 2, 3)
fool(c=1, b=2, a=3) # You have to type all the keyword
fool(1, b=2, c=3) #fool(1, b=2, 3) #This will be error
# Its about Positional Arguments, can't use another positional args after keyward arguments

#Default Argument
def fool(a, b, c, d=4): # You have to put in the last arguments
    print(a, b, c, d)

fool(1, 2, 3)
fool(1, 2, 3, 7) #can change the value

def fol(a, b, *args, **kwargs): 
    # * It can pass any number of positional arguments to your function
    # ** You can pass any keyword of any arguments
    print(a, b)
    for args in args:
        print(args)
    for key in kwargs:
        print(key, kwargs[key])

fol(1, 2, 3, 4, 5, six=6, seven=7)

def fool(a, b, *, c, d): # Parameter after * must be a keyword argument
    print(a, b, c, d)

 # fool(1, 2, 3, 4) Wrong
fool(1, 2, c=3, d=4)


def pol(*args, last):
    for arg in args:
        print(arg)
    print(last)

pol(1, 2, 3, last=100) # *args will make a new line 


# Unpacking Arguments
def fool(a, b, c): 
    print(a, b,c)


my_list = [2, 4, 5]
my_tuple = (0, 1, 2)
my_dict = {'a':1, 'b':2, 'c':3}
fool(*my_list)
fool(*my_tuple)
fool(*my_dict)

#Global and Local Variable
def fop():
    global number # Making the the Local to Global (Can modify to Global)
    x = number
    number = 3 # Local Variable
    print('number inside function:', x)

number = 0 # This is global variable
fop() # This change the number 0 to 3
print(number) # That's why the answer is 3


#Immutable Object : Interger (5), Float(7.5), String ("Hello"), Tuple (1, 2), Boolean (True), 
def co(x):
    x = 5

var = 10
co(var)
print(var) #The Refrences doesnt change


#Mutable object
def ci(a_list):
   # a_list = [200, 300, 400] # Cant rebind a mutable Object (Change the refrences variable to a new object )
    a_list += [200, 300, 400] # Instead of using append u can use +=
    a_list.append(4)
    a_list[0] = -100
    
my_list2 = [1, 2, 3]
ci(my_list2)
print(my_list2)
