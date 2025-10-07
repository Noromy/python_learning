from . import DataBase
from .Util import random_string
import random
import string
import time
import os
import json



def create_database():
    author = input("Input Author name: ")
    tittle = input("Input book's tittle: ")
    year = int(input("Input book's year: "))
    pk = random_string(6)
    data_added = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())


    data_str = {
        "Pk" : pk, "Date_added" : data_added, "Author" : author, "Tittle" : tittle, "Year" : year
    }
    print(data_str)
    
    try:
        with open(DataBase.UserFolder, "w", encoding="utf-8") as file:
            json.dump([data_str], file, separators=(',', ':'), indent=4)
    except Exception as e:
        print(f'Error: {e}')

def read(**kwargs):
    try:
        with open(DataBase.UserFolder, "r") as file:
            data = json.load(file)
            index = kwargs.get("index")
            if index is not None:
                if 0 <= index < len(data):
                    item = data[index]
                    print("="*100)
                    print(f"{'No':4}  |  {'Tittle':40}  |  {'Author':20}  |  {'Year':5}")
                    print("-"*100)
                    print(f"{index + 1:4}  |  {item['Tittle'][:40]:<40}  |  {item['Author'][:20]:<20}  |  {item['Year']}")
                    print("="*100)
                    return item
                else:
                    print("❌ Index out of range.")
                    return None
            if isinstance(data, list):  # Pastikan ini list of dicts
                return data
            else:
                print("Invalid JSON structure: Expected a list.")
                return []
    except FileNotFoundError:
        print("Database not found. Please create the database first.")
        return False
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
def write(file_path, data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data_lama = json.load(file)
            except Exception as e:
                print(f'Error reading eisting data: {e}')              
    else:
        data_lama = []

    data_lama.append(data)

    with open(file_path, 'w') as file:
        json.dump(data_lama, file, separators=(',', ':'), indent=4)
    print("Data successfully added.")

    read()

def update(data_file):
    try:
        with open(DataBase.UserFolder, "w") as file:
                json.dump(data_file, file, indent=2)
                print("Book updated successfully.")
    except Exception as e:
        print(f'Error Updating data: {e}')
