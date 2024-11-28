from jelolt import jelolt
def main():
    adat = beolvas()
    masodik(adat)
    harmadik(adat)
    o = negyedik(adat)
    otodik(adat, o)
    hatodik(adat)
def beolvas():
    adat = []
    with open("./szavazatok.txt", "rt", encoding="utf-8") as f:
        for sor in f.readlines():
            d = sor.strip().split(' ')
            adat.append(jelolt(d[2],d[3],d[0],d[1],d[4]))
    return adat
def masodik(e):
    print("2. feladat")
    print(f"A helyhatósági választáson {len(e)} képviselőjelölt indult.")
def harmadik(e):
    print("3. feladat")
    kep = input("Keresett képviselőjelölt: ").split(' ')
    i = 0
    while i < len(e) and (e[i].vezeteknev != kep[0] or e[i].keresztnev != kep[1]):
        i += 1
    if i < len(e):
        print(f"{' '.join(kep)} {e[i].szavazatok} szavazatott tudott begyűjteni.")
    else:
        print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
def negyedik(e):
    print("4. feladat")
    db = 0
    for i in e:
        db += int(i.szavazatok)
    print(f"A választáson {db} állampolgár, a jogosultak {round(db/12345,4)*100}%-a vett részt.")
    return db
def otodik(e,o):
    print("5. feladat")
    rov = {"GYEP": "Gyümölcsevők Pártja",
           "HEP": "Húsevők Pártja",
           "TISZ": "Tejivók Szövetsége",
           "ZEP": "Zöldségevők Pártja",
           "-": "Független jelöltek"}
    partok = {}
    for i in e:
        if not partok.get(i.tamogato):
            partok.update({i.tamogato:int(i.szavazatok)})
        else:
            partok[i.tamogato] += int(i.szavazatok)
    for part,szavatok in partok.items():
        print(f"{rov[part]}= {round(szavatok/o*100,2)}%")

def hatodik(e):
    print("6. feladat")
    mI = 0
    for i in range(len(e)):
        if int(e[i].szavazatok) > int(e[mI].szavazatok):
            mI = i
    for j in e:
        if j.szavazatok == e[mI].szavazatok:
            print(f"{j.vezeteknev} {j.keresztnev} |{j.szavazatok}| - ", end="")
            if j.tamogato == "-":
                print("független")
            else:
                print(j.tamogato)
if __name__ == "__main__": #lsc.io/98b74bd0
    main()
