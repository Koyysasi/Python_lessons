def main():
    print("INPUT: ")
    a = input("Adj meg valami bevitelt:")
    print("KIMENET:")
    print(a)
    print("VÁLTOZÓK/ADATTIPUSOK")
    egeszSzam = int(123)
    tortSzam = float(3.14)
    szoveg = str("B l a b l a")
    logikai = bool(True)
    print("Egész szám: "+str(egeszSzam))
    print("Tört szám : "+str(tortSzam))
    print("Szöveg    : "+szoveg)
    print("Logikai   :"+str(logikai))
    print("COMPLEXEBB ADATTIPUSOK (GYÜJTEMÉNYEK)")
    tomb = []   # TOMB = LISTA
    lista = list()    # SORRENDEZETT,      MODOSITHATÓ,     DUPLIKÁLT ELEMEKKEK
    halmaz = set()    # NEM RENDEZETT, NEM MÓDOSÍTHATÓ, NEM DUPLIKÁLT ELEMEKKEL
    csomag = tuple()  # SORRENDEZETT,  NEM MÓDOSÍTHATÓ,     DUPLIKÁLT ELEMEKKEL
    konyvtar = dict() # SORRENDEZETT,      MÓDOSÍTHATÓ, NEM DUPLIKÁLT ELEMEKKEL

    lista = ["Alma", 23, "Béka", True, 1.25] # TÖBB FÉLE ADATTIPUS IS LEHET
    halmaz = {1, 2, 3}  # A HALMAZOK MEGFELELŐK, TÖBBSZÖR SZEREPLŐ ELEMEK KISZŰRÉSÉRE
    halmaz2 = {3, 4, 5} # ILLETVE, ELVÉGEZHETŐ RAJTUK, MATEMATIKAI MÚVELETEK
    csomag = (1,2,3)    # HASZNOS KOORDINÁTÁKHOZ, VEKTOROKHOZ, EGYSZERÜ SZÁMOKHOZ
    konyvtar = {"Alma"  :  315, # MEGFELELŐ, OLYAN FELSOROLÁSOKRA, AHOL EGYEZŐ KULCS
                "Körte" :  500, # SZÜKSÉGES, MINT PL FELHASZNÁLÓ ADATBÁZISNÁL,
                "Csirke": 1500} # VAGY AKÁR TERMÉKEKNÉL
    print("MATEMATIKAI MÜVELETEK:\n"
          "\tÖSSZEADÁS:          +\n"
          "\tKIVONÁS:            -\n"
          "\tSZORZÁS:            *\n"
          "\tOSZTÁS:             /\n"
          "\tKEREKÍTETT OSZTÁS: //\n"
          "\tHATVÁNYOZÁS:       **\n")
    print("LOGIKAI ÉS BIT MÜVELETEK:\n"
          "\tAND:              and\n"
          "\tOR:                or\n"
          "\tNOT:              not\n"
          "\tBIT AND:            &\n"
          "\tBIT OR:             |\n"
          "\tBIT XOR:            ^\n"
          "\tBIT NOT:            ~\n"
          "\t0BIT TOLÁS BALRA:  <<\n"
          "\t0BIT TOLÁS JOBBRA: >>\n")
    print(f"SZÖVEG FÜGGVÉNYEK: ({szoveg})\n"
          f"\tKarakterszám:              len = {len(szoveg)}\n"
          f"\tÜreskarakterek törlése : strip = {szoveg.strip()}\n"
          f"\tFeldarabolás:       split(SEP) = {szoveg.split(' ')}\n"
          f"\tMivel kezdődik:  startswith(K) = {szoveg.startswith('a')}\n"
          f"\tMivel végződik:    endswith(K) = {szoveg.endswith('a')}\n"
          f"\tKapitalizálás:      capitalize = {szoveg.capitalize()}\n"
          f"\tCsupa nagybetü:          upper = {szoveg.upper()}\n"
          f"\tCsupa kisbetü:           lower = {szoveg.lower()}\n"
          f"\tCsupa nagybetü-e?:     isupper = {szoveg.isupper()}\n"
          f"\tCsupa kisbetü-e?:      islower = {szoveg.islower()}\n"
          f"\tÖsszefűzés tömbböl:    join(T) = {szoveg.join(' ')}\n"
          f"\tHány darab valami:    count(K) = {szoveg.count('k')}\n")
    print(f"LISTA FÜGGVÉNYEK: {lista}\n"
          f"\tHossz:             len = {len(lista)}")
    lista.append("Brekeké")
    print(f"\tHozzáadás:   append(L) = {lista}")
    lista.remove("Béka")
    print(f"\tEltávolítás: remove(L) = {lista}")
    lista2 = [1, 54, 513, 76, 35, -52 , -64, 0]
    lista2.sort()
    print(f"\tRendezés:         sort = {lista2}")
    lista.insert(3, "Brekekekekekke")
    print(f"\tBeszúrás:  insert(I,L) = {lista}")
    print(f"\tHelykeresés:  index(L) = {lista.index(True)}")
    lista.reverse()
    print(f"\tMegfordítás:      reverse = {lista}")
    print("FÜGGVÉNY VISSZATÉRÉSI ÉRTÉKKEL ÉS PARAMÉTERREL:")
    print(f"\tsajatFuggveny(S) = {sajatFuggveny('brekekek')}")
    print("KÜLSŐ MODULOK HASZNÁLATA ALIASSAL")
    import os
    from random import randint as r
    from math import sin
    print("\tos module:        whoami = ", end="")
    os.system("whoami")
    print("\tos module: echo %RANDOM% = ",end="")
    os.system("echo %RANDOM%")
    print(f"\trandint as r:    r(1,15) = {r(1,15)}")
    print(f"\tsin from math: sin(r(0,360) = {sin(r(0,360))}")
    print("SAJÁT KÜLSŐ MODULOK HASZNÁLATA")
    import sajat
    beka = sajat.sajatos()
    print(f"\t sajat.sajatos() = {beka}")
def sajatFuggveny(parameter):
    return str(parameter)+" jaj"

if __name__ == "__main__":
    main()
    