# Calculator
from Operators import basic, advanced

def utama():
    print("=== Kalkulator CLI Modular ===")
    print("Operatornya ;'tambah', 'kurang', 'kali', 'bagi', 'pangkat', 'akar'")
    
    ParaOP = ['tambah', 'kurang', 'kali', 'bagi', 'pangkat', 'akar']
    
    while True:
        Opertor = input("Masukkan Operator(exit : untuk keluar) : ").strip()
        if Opertor == "exit":
            break
        
        if Opertor not in ParaOP:
            print("Operator tidak dikenali, harap masukkan operator yang sesuai!")
            continue

        try:
            if Opertor == "akar":
                sqrt = float(input("Masukkan angka :"))
                result = advanced.akar(sqrt)
            else:
                a = float(input("Angka pertama : "))
                b = float(input("Angka kedua : "))
                if Opertor == "tambah":
                    result = basic.tambah(a, b)
                elif Opertor =="kurang":
                    result = basic.kurang(a, b)
                elif Opertor == "kali":
                    result = basic.kali(a, b)
                elif Opertor == "bagi":
                    result = basic.bagi(a, b)
                elif Opertor == "pangkat":
                    result = advanced.pangkat(a, b)
            print(f'Hasil : {result}')
        
        except Exception as e:
            print(f'Error : {e}')

if __name__ == "__main__":
    utama()

