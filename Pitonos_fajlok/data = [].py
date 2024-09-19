import os

data = []

def main():
    print("")
    inp = input("Regisztráció (0) vagy bejelentkezés (1) ")
    while(not inp.isnumeric()):
        inp = input("Regisztráció (0) vagy bejelentkezés (1) - Érvényes értéket adj meg! ")
    while(not len(inp) == 1 or int(inp) < 0 or int(inp) > 1):
        inp = input("Regisztráció (0) vagy bejelentkezés (1) - Érvényes értéket adj meg! ")
    if str(inp) == "0":
        print("")
        print("Regisztráció")
        u = input("Felhasználónév: ")
        p = input("Jelszó: ")
        register(u, p)
    if str(inp) == "1":
        print("")
        print("Bejelentkezés")
        u = input("Felhasználónév: ")
        p = input("Jelszó: ")
        siker = login(u, p)
        print(siker)

def register(u, p):
    data1 = [u, p]
    for i in data:
        for j in i:
            if not j == u:
                pass
            else:
                print("Ez a felhasználónév már használatban van!")
                main()
                break
    data.append(data1)
    print("Sikeres regisztráció!")
    os.system('cls')
    main()

def login(u, p):
    for i in data:
        print(i)
        if i[0] == u:
            if i[1] == p:
                print("")
                print("Bejelentkezve")
                print("Üdvözlünk, " + u + "!")
                return True
            else:
                print("Helytelen jelszó!")
                main()
    for i in data:
        for j in i:
            if j == u:
                return
            else:
                pass
    print("Felhasználó nem található")
    main()


if __name__ == "__main__":
    main()
    data = []