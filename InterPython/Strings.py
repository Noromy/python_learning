# Strings is immutable
my_strings = 'Hello, World!' or "I'm learning Python!"
my_strings1 = '''This is a multi-line string. # "/"
It can span multiple lines.
'''
# "\"  make it one line
print(my_strings)
print(my_strings1)

char = my_strings[1:4] #Accessing characters
#Reverse [::-1]
print(char) 

my_strings = my_strings.strip() #Removing whitespace
print(my_strings.startswith('Hello')) #Check if string starts with 'Hello'
print(my_strings.endswith('!')) #Check if string ends with '!'
print(my_strings.find('World')) #Find the position of 'World' if doesnt found -1
print(my_strings.count('o')) #Count occurrences of 'o'  
print(my_strings.replace('World', 'Python')) #Replace 'World' with 'Python'


my_list = my_strings.split() #Splitting string into list
print(my_list)

new_string = ' '.join(my_list) #Joining list into string
print(new_string)

my_list = ['a'] * 1000

import timeit

my_list = ['a'] * 1000

# Versi +=
bad_time = timeit.timeit("s=''; [s:=s+i for i in my_list]", globals=globals(), number=1000)

# Versi join
good_time = timeit.timeit("''.join(my_list)", globals=globals(), number=1000)

print(f"Versi += : {bad_time:.6f} detik")
print(f"Versi join: {good_time:.6f} detik")


# %, .format(), f-strings
# old formatting style
var = 3.2
my_string = "The variable is %s" % var
                       #     %d = Number
                       #    %.2f = Float (2f means only show 2 Number after dots)
print(my_string)
my_string = "The Variable is {}".format(var)
                        #    {:.2f}
print(my_string) 

#new Style
my_string = f"the variable is {var}"

