from auth import login, Register, show_user


def main():
    print("=== Sistem Login Sederhana ===")



    while True:
        print("\n Daftar menu : [login] [register] [daftar users] [exit]")
        Menu = input("\n Pilih menu : ").strip().lower()
        
        if Menu == "login":
            return login()
        elif Menu == "register":
            return Register()
        elif Menu == "daftar users":
            return show_user()
        elif Menu == "exit":
            print("Sampai jumpa kembali !")
            break
        else:
            print("Pilihan tidak tersedia")

    print("Terlalu banyak percobaan, Program di hentikan")
    return False
        
if __name__ == "__main__":
    main()