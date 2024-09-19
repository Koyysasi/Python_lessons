def main():

    # KOR

    kor = input("Hány éves vagy? ")
    while not(kor.isdigit()) or (0 > int(kor) > 150):
        if (kor.isdigit()):
            if (int(kor) < 0) or (int(kor) > 150):
                kor = input("Hány éves vagy? (0 és 150 között) ")
        else:
            kor = input("Hány éves vagy? (számot adj meg) ")

    # NÉV
            
    nev = str(input("Mi a neved? (vezetéknév keresztnév) "))
    nev.strip()
    list = nev.split()
    while not len(list) == 2 or not(list[0].isalpha()) or not(list[1].isalpha()):
        nev = str(input("Mi a neved? (vezetéknév keresztnév) "))
        list = nev.split()
    nev = " ".join(list)

    # TELEFON

    telefonszam = str(input("Telefonszám? "))
    while not(len(str(telefonszam)) == 11) or not(telefonszam.startswith("06")) or not(str(telefonszam).isdigit()):
        if not len(str(telefonszam)) == 11:
            telefonszam = str(input("Telefonszám? (11 számból kell álljon) "))
            pass
        if not str(telefonszam).isdigit():
            telefonszam = str(input("Telefonszám? (SZÁM bruh) "))
            pass
        if not str(telefonszam).startswith("06"):
            telefonszam = str(input("Telefonszám? (nem magyar vagy :c ) "))
            pass
        else:
            pass


    # PRINT
    
    print(kor)
    print(nev)
    print(telefonszam)

if __name__ == "__main__":
    main()