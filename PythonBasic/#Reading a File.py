#Reading a File

# open("Contoh file.txt", "r")  # Open a file in read mode
 # open("Contoh file.txt", "a")  # Open a file in append mode
  # open("Contoh file.txt", "w")  # Open a file in write mode
contoh_file = open("Contoh file.txt", "r")
# contoh_file = open("Contoh file1.txt", "w") #Create a new file
# print(contoh_file.readable())  # Check if the file is readable
# print(contoh_file.readlines()) # Read all lines in the file
# print(contoh_file.readline())  # Read the first line of the file
for line in contoh_file.readlines():  # Iterate through each line in the file
   print(line) 
    # print(line.strip())  # Print each line without extra spaces or newlines
  # Find the index of the word "ganteng" in each line
  # contoh_file = open("Contoh file.txt", "a") #Append mode is to add the last list of the list
 # contoh_file.write("Dafa - Public\n")  taruh di line terbaru (Append untuk menambah list)

contoh_file.close()  # Close the file after reading
# contoh_file.write("Dafa - Public\n")  # Write to the file (this will overwrite the file if opened in write mode)
# Writing is able to create a new file too

