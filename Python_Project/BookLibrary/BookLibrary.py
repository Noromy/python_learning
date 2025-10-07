import os
import Data_Base as db

if __name__=="__main__": 
    system_operation = os.name
    match system_operation:
        case "posix": os.system("clear")
        case "nt" : os.system("cls")

    print("WELCOME TO THE PROGRAM")
    print("DATABASE BOOK LIBRARY")
    print("========================")

    # Checking database existence
    db.init_console()

    while True:

        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Remove book")
        print("5. Exit")
        
        choice = input("Enter your list choice (1-5): ")

        match choice:
            case "1": db.read_control()
            case "2": db.create_control()
            case "3": db.update_control()
            case "4": print("Update Data Book")
            case "5": print("Exit");break
            case _: print("Invalid choice. Please try again.")
        
        is_done = input("Apakah Selesai (y/n)? ").lower().strip()
        if is_done == "y":
            break

