color = input("Enter a color: ")
noun = input("Enter a noun: ")
animal = input("Enter an animal: ")



print("Mataram is " + color)    
print(noun + "  is blue")
print("pasopati " + animal)

num1 = 5
print(str(num1) + " is a number")

float_num = 3.14
print(str(float_num) + " is a float number")

int_num = 10
print(str(int_num) + " is an integer")

phrase = "Hello, World!"

print(phrase[0]) # Access the first character
print(phrase.index("H")) 
print(phrase.upper()) 
print(phrase.upper().isupper())
print(len(phrase))
print(phrase.lower())
print(phrase.replace("World", "Python")) 

def capitalize_one_word(sentence, position=0): # Function to capitalize a word at a specific position
    """Capitalize the word at the specified position in a sentence."""
    words = sentence.split() # Split the sentence into words
    if 0 <= position < len(words): # Check if position is valid
        words[position] = words[position].upper() # Capitalize the word at the specified position
    return ' '.join(words) # Join the words back into a sentence

# Example usage
sentence = "i am learning python"
result = capitalize_one_word(sentence, position=2)  # Capitalize the 3rd word (index 2)
print(result)  # Output: i am LEARNING python
