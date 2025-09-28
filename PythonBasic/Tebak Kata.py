secret_word = "Bebek"
guess = "Anjing"
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Tebak hewan apa: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Maaf, kamu kehabisan tebakan!")
else:
    print("You win!")


#For Loop
friends = ["Rizky", "Fathur", "Dimas", "Adit"]
len(friends)  # Get the number of friends
for index in range(len(friends)): # Loop through the indices
    # Print each friend's name
    print(friends[index])
    if index == 0: # Check if it's the first friend
        print("This is the first friend in the list.") # Additional context for the first friend
    else:
        print("This is not the first friend.")

#Exponential Calculation

# This code calculates the exponential of 2 raised to the power of 3
def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
    
# Example usage of the function
print(raise_to_power(3, 4))  # Output: 81

#List of Numbers
# This code defines a 2D list (grid) of numbers and prints each number in
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
] # A 2D list representing a grid of numbers

for row in number_grid: # Loop through each row in the grid
    for col in row: # Loop through each column in the row
        print(col) # Print each number in the grid

#col is for 1 by 1
#row is for all the numbers in a row



#Basic Translator
def translate(phrase): # This function translates a phrase by replacing vowels with 'g' or 'G'
    translation = "" # Initialize an empty string for the translation
    for letter in phrase:
        if letter.lower() in "aiueo":
            if letter.isupper(): # If the letter is uppercase
                translation += "G"
            else: # If the letter is lowercase
                translation += "g"
        else: # If the letter is not a vowel
            translation += letter
    return translation #  Return the translated phrase

print(translate(input("Enter a Phrase: ")))