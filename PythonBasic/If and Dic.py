is_male = False
is_tall = True

if is_male and is_tall:
    print("Hey, man")
elif is_male and not(is_tall):
    print("Hey, short")
elif not is_male and is_tall:
    print("Hey, tall")
else:
    print("You neither male nor tall")



def max_num(num1, num2, num3): # Function to find the maximum of three numbers
    """Return the maximum of three numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(6, 5, 2))

1 == 2 # Same
1 != 2 # Not same
 
# Dictionary to map month abbreviations/num to full names
monthConversation = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversation["Jan"])  # Output: January
print(monthConversation.get("Nob", "Salah goblok kamu sekolah dari mana"))  # Output: February


i = 1
while i <= 10: # Loop from 1 to 10
    print(i)
    i += 1 # Increment i by 1

print("Loop selesai")