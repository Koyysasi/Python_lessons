import os

os.system("cls")


felh = []
pw = []


def main():
    q1 = ''
    while q1 != '0':
        q1 = input("Bejelentkezés(0) -||- Regisztráció(1) -||- Kilépés(2)\n    >>>")
        if q1 == "0":
            login()
        if q1 == "1":
            regist()
        if q1 == "2":
            break
        

def login():
    name = input("Írd be a neved: ")
    if name in felh:
        password = input("Írd be a jelszavad: ")
        if password in pw:
            print(f"Sikeresen bejelentkeztél")

            main()


def regist():
    nev = input("írd be a neved: ")
    jelsz = input("Írd be a jelszavad: ")
    felh.append(nev)
    pw.append(jelsz)
    
    q1 = input("Bejelentkezés(0) -||- vissza(1)\n    >>>")
    while q1 == "0" or q1 == "1" or q1 == "2":
        if q1 == "0":
            login()
        if q1 == "1":
            main()

if __name__ == "__main__":
    main()