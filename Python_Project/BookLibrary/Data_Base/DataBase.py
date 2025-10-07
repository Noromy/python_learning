from . import Operation
import os
import json


DB_NAME = "database.json"

Folder = os.path.join(os.path.dirname(__file__), "BookData")
UserFile = DB_NAME
UserFolder = os.path.join(Folder, UserFile)




def init_console():
    print("Checking database")
    try:
        with open(UserFolder, "r") as file:
            print("Database found!")
    except:
        print("Database not found, silahkan membuat database baru.")
        if not os.path.exists (Folder):
            os.makedirs(Folder)
        Operation.create_database()
