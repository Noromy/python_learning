import os

if __name__=="__main__": 
    system_operation = os.name
    while True:
        match system_operation:
            case "posix": os.system("clear")
            case "nt" : os.system("cls")

        print("WELCOME TO THE PROGRAM")
        print("DATABASE BOOK LIBRARY")
        print("========================")

        print("1. View Books")
        print("2. Add Book")
        print("3. Remove book")
        print("4. Update book")
        print("5. Exit")
        
        choice = input("Enter your list choice (1-5): ")

        print("\n===================\n")

        match choice:
            case "1": print("View Data Book")
            case "2": print("Add Data Book")
            case "3": print("Remove Data Book")
            case "4": print("Update Data Book")
            case "5": print("Exit");break
            case _: print("Invalid choice. Please try again.")

        print("\n===================\n")
        
        is_done = input("Apakah Selesai (y/n)? ").lower().strip()
        if is_done == "y":
            break
