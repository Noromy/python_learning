import json
import os
Folder = os.path.join(os.path.dirname(__file__), "Log_User")
UserFile = "users.json"
UserFolder = os.path.join(Folder, UserFile)



if not os.path.exists (Folder):
    os.makedirs(Folder)

def load_users():
    if not os.path.exists (UserFolder):
        with open(UserFolder, "w") as File:
            json.load({}, File)
    with open(UserFolder, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
    
def save_user(users):
    with open(UserFolder, "w") as f:
        json.dump(users, f, indent=4, separators=(",", ":")) 
    
def Register():
    users = load_users()
    username = input("Masukkan username : ").strip()
    if username in users:
        print("Maaf username sudah terdaftar")
        return
    password = input("Masukkan Password : ").strip()
    users[username] = password
    save_user(users)
    print("Registrasi berhasil")

def login():
    attemps = 3
    users = load_users()
    while attemps > 0:
        username = input("Masukkan username : ").strip()
        password = input("Masukkan pasword : ").strip()
        if username not in users:
            attemps -= 1
            print("username salah")
        elif users.get(username) != password:
            attemps -= 1
            print("Password salah")
        else:
            print(f"Login berhasil, Selamat datang {username}")
            return True
    print('Terlalu banyak percobaan. Program di hentikan')
    return False


def show_user():
    users = load_users()
    print("Daftar sudah terdaftar")
    for user in users:
        print (f" - {user}")

print("test")
    