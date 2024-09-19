felhasznalonevek = []
jelszok = []

def Belepes(felhnev, jelszo):
    belepett = False
    i = 0
    while belepett == False and i < len(felhasznalonevek):
        if felhnev == felhasznalonevek[i]:
            # megvizsgáljuk, hogy tartozik-e hozz- jelszó is
            if jelszo == jelszok[i]:
                belepett = True
            else:
                print("Nem jó a felhasználónévhez tartozó jelszó")
    i += 1
    if belepett == True:
        print("Sikeresen beléptél")
        return True
    else:
        print("Sikertelen belépés")


def Regisztracio(felhnev, jelszo):
    vanemar = False
    i = 0
    while i < len(felhasznalonevek) and vanemar:
        if  felhnev == felhasznalonevek[i]:
            vanemar = True
            print("Sikertelen regisztráció, műr van ilyen felhasználó")
            return False
        i += 1

    if vanemar == False:
        felhasznalonevek.append(felhnev)
        jelszok.append(jelszo)
        print("Sikeres regisztráció")
        return True

def main():
    siker = False
    while siker == False:
        valasz = input("Belénél vagy regisztrálnál? (B/R)")
        if valasz.upper() == "B":
            felhnev = input("Add meg a felhasználóneved: ")
            jelszo = input("Add meg a jelszavad: ")
            siker = Belepes(felhnev,jelszo)
        elif valasz.upper() == "R":
            felhnev = input("Add meg a felhasználóneved: ")
            jelszo = input("Add meg a jelszavad: ")
            Regisztracio(felhnev, jelszo)

if __name__ == '__main__':
    main()