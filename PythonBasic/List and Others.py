lucky_number = [2, 3] #List of lucky numbers
friend = ["Cecep", "Ujang", "Dudung", "Asep", "Deden"]
friend[1] = "Sadewo"
friend.extend(lucky_number) #Extend the list with lucky_numbers
friend.append("Budi") #End of the list #Adding List
friend.insert(2, "Jajang") #Insert at index 2
friend.remove("Dudung") #Remove "Dudung" from the list
friend.pop() #Remove the last item from the list
print(friend)
print(friend.count("Cecep")) #Count how many times "Cecep" appears
print(friend.index("Cecep")) #Find the index of "Cecep"
friend.clear() #Clear the list


lucky_numbers = [1, 6, 3, 4, 5]

lucky_numbers.sort()
print(lucky_numbers) #Sort the lucky_numbers list
lucky_numbers.reverse()
print(lucky_numbers) #Reverse the lucky_numbers list
lucky_number2 = friend.copy() #Create a copy of the friend list


coordinate = (4, 5), (6, 7), (8, 9) #Tuple of coordinates
print(coordinate[0])  #You can not change the value of a tuple

def sayhi(name, age): #Function to greet a person
    """This function greets a person with their name and age."""
    print("Hello, " + str(name) + ". You are " + str(age) + " years old.")

sayhi("Mike", 35)

def cube(num):
    return num*num*num #Function to calculate the cube of a number

result = cube(3)
print(result)