myList = ["banana", "apple", "orange"]
print(myList)

myList2 = [5, True,"grape", "kiwi", "melon"]
print(myList2)

item = myList[1] # This is the second item in myList
print(item)

for i in myList:
        print(i)

if "banana" in myList:
    print("Found banana!")
else:
    print("Banana not found.")

myList = [0] * 5 # Create a list with 5 zeros
print(myList)

mylist = [1, 3, 4, 5, 6]
a = mylist[1:4] # Slicing the list from index 1 to 3
a = mylist[:1] # Slicing the list from the start to index 0
a = mylist[1:] # Slicing the list from index 2 to the end
a = mylist[:] # Slicing the whole list
a = mylist[::1] # Slicing the whole list with step
a = mylist[::2] # Slicing the whole list with step of 2
a = mylist[::-1] # Reversing the list
# Number that Slicing (The last number) not included
print(a)

list_copy = mylist.copy() # Copying the list
            # list(mylist) # Another way to copy the list
            # mylist[:] # Another way to copy the list
list_copy.append(7) # Adding 7 to the copied list
print(list_copy)
print(mylist) # Original list remains unchanged

testing_looping = [x*x for x in mylist] # List comprehension to create a new list with squares of the original list
print(testing_looping)