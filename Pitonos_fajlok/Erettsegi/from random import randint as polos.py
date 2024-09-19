from jelolt import Jelolt

def main():
    adat = beolvas()
    for i in adat:
        print(i)
    masodik(adat)
    harmadik(adat)
    o = negyedik(adat)
    #otodik(adat, o)
    hatodik(adat)

def beolvas():
    adat = []
    with open("./szavazatok.txt", "rt", encoding="utf-8") as f:
        for sor in f.readlines():
            d = sor.strip().split(" ")
            adat.append(Jelolt(d[2], d[3], d[0], d[1], d[4]))
    return adat

def masodik(e):
    print("2. feladat")
    print(f"A helyhatósági választáson {len(e)} képviselő indult.")

def harmadik(e):


    print("3. feladat")
    kep = input("Keresett képviselő:").split(' ')
    while len(kep) != 2:
        kep = input("Keresett képviselő:").split(' ')
    i = 0
    while i < len(e) and (e[i].vezeteknev != kep[0] or e[i].keresztnev != kep[1]):
        i += 1
    if i < len(e):
        print(f"{' '.join(kep)} {e[i].szavazatok} szavazatot kapott")
    else:
        print("Ilyen képviselő nem szerepel a nyilvántartásban!")

def negyedik(e):
    print("4. feladat")
    db = 0
    for i in e:
        db += int(i.szavazatok)
    print(f"A választáson {db} állampolgár, a jogosultak {round(db/12345,4)*100}%-a szavazott")
    return db

def otodik(e, o):
    print("5. feladat")
    partok = {}
    rov = {"GYEP" : "Gyümölcsevők pártja", "ZEP" : "Zöldségevők pártja", "TISZ" : "Tejivók szövetsége", "-" : "Független jelöltek"}
    for i in e:
        if not partok.get(i.tamogato):
            if i.tamogato == "-":
                partok.update({"Független jelöltek: ":int(i.szavazatok)})
            else:
                partok.update({i.tamogato:int(i.szavazatok)})
        else:
            partok.update[i.tamogato] += int(i.szavazatok)
    for part,szavazatok in partok.items():
        print(f"rov{[part]} = {round(szavazatok/o*100,2)}%")

def hatodik(e):
    str = ""
    names = []
    szavazatok = 0
    for i in e:
        if int(i.szavazatok) > int(szavazatok):
            szavazatok = i.szavazatok
            str = i.vezeteknev+" "+i.keresztnev
        else:
            continue
    for i in e:
        if int(i.szavazatok) == int(szavazatok):
            names.append(i.vezeteknev+" "+i.keresztnev)
    names.append(str)
    print(names)


if __name__ == "__main__":
    main()