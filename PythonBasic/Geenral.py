#This is a test file
print("Comments are fun")
'''
This is a multi-line comment
that spans multiple lines.
'''

1 == 2 # Same
1 != 2 # Not same

integer_variable = 5  # This is an integer variable
float_variable = 5.5  # This is a float variable
string_variable = "Hello"  # This is a string variable

try: # This code checks if the user input is a valid integer
    Value = 10/0  # This line will raise a ZeroDivisionError
    number = int(input("Enter a number: "))  # Prompt user for input and convert to integer        
    print("Selamat datang, kamu memasukkan angka:", number)  # Print a welcome message with the number
except ZeroDivisionError as err: # Handle the case where input is not a valid integer
    print("Kamu masukkan angka 0.")
except ValueError: # Handle the case where input is not a valid integer
    print("Kamu masukkan bukan angka.")

