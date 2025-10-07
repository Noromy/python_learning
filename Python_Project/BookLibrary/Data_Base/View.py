from . import Operation
from . import DataBase
import json




def update_control():
    read_control()
    print("\nChoose the book number to update: ")
    no_book = int(input("book number: "))
    data_file = Operation.read()
    Operation.read(index=no_book - 1)
    if 1 <= no_book <= len(data_file):
        book = data_file[no_book - 1]
        print(f"\nCurrent Data:")
        print(f"Tittle : {book['Tittle']}")
        print(f"Author : {book['Author']}")
        print(f"Year   : {book['Year']}")


        new_title = input("New title (leave blank to keep): ")
        new_author = input("New author (leave blank to keep): ")
        while True:
            new_year = input("Input book's year (leave blank to keep): ")
            if not new_year:
                new_year = None
                break
            if  new_year.isdigit() and len(new_year) == 4:
                new_year = int(new_year)
                break
            else:
                print("❌ Year must be a 4-digit number. Please try again.")
 

        if new_title: book['Tittle'] = new_title
        if new_author: book['Author'] = new_author
        if new_year: book['Year'] = int(new_year)

    else:
        print("Invalid book number.")
    Operation.update(data_file)



def create_control():
    print("\n"+"="*100)
    print("Create new a book \n".center(100))
    pk = Operation.random_string(6)
    data_added = Operation.time.strftime("%Y-%m-%d-%H-%M-%S%z",Operation.time.gmtime())
    author = input("Input Author name: ")
    tittle = input("Input book's tittle: ")
    while True:
        try:
            year = int(input("Input book's year: "))
            if len(str(year)) == 4:
                break
            else:
                print("year must be 4 digits. please try again.")
        except ValueError:
            print("Invalid input for year. Please enter a number.")
    data_str = {
        "Pk" : pk, "Date_added" : data_added, "Author" : author, "Tittle" : tittle, "Year" : year
    }
    print(data_str)
    Operation.write(DataBase.UserFolder, data_str)
    



def read_control():
    data_file = Operation.read()
    index = "No"
    author = "Author"
    tittle = "tittle"
    year = "year"


    # Header
    print("\n"+"="*100)
    print(f"{index:4}  |  {tittle:40}  |  {author:20}  |  {year:5} ")
    print("-"*100)

    # Data
    for index,data in enumerate(data_file, start=1):
        pk = str(data.get("Pk", ""))
        date_added = str(data.get("Date_added", ""))
        author = str(data.get("Author", ""))
        tittle = str(data.get("Tittle", ""))
        year = str(data.get("Year", ""))
        print(f"{index:4}  |  {tittle[:40]:<40}  |  {author[:20]:<20}  |  {year:5}", end="\n")

    # Footer
    print("="*100+"\n")

def delete_control():
    read_control()
    print("\nChoose the number of the book to delete: ")
    no_book = int(input("book number: "))
    data_file = Operation.read()
    if 1 <= no_book <= len(data_file):
        book = data_file[no_book - 1]
        print("\n"+"="*100)
        print(f'You are about to delete the book: ')
        print(f'Tittle\t : {book["Tittle"]}')
        print(f'Author\t : {book["Author"]}')
        print(f'Year\t : {book["Year"]}')
        confirm = input(f"Are you sure you want to delete '{book['Tittle']}' by {book['Author']}? (y/n): ").lower()
        if confirm == 'y':
            data_file.pop(no_book - 1)
            Operation.update(data_file)
            print("Book deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid book number.")


