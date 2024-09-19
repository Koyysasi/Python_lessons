def main():
    a = "LogIscoOl"
    print(a)
    print(a.isupper()) # csupa nagybetű?
    print(a.islower()) # kisbetűs?
    print(a.upper())
    print(a.lower())
    print(len(a))
    print(a.count('o'))
    print(a.lower().count('o'))
    print(a.isdigit())
    b = "megy a roka az erdoben"
    print(b)
    print(b.capitalize())
    print(b[0].isupper()) # első betű nagybetű?
    print(b.title()) # string: minden szó nagy kezdő betű
    print(b.istitle()) # bool: nagy betű-e minden új szó
    print(b.startswith("megy")) # bool: ezzel kezdő(dik-e?
    print(b.endswith(".")) # bool: ezzel végződik-e?
    print(b.isspace()) # teljesen üres-e?
    print()
    c = 'NEV, KOR, DATUM, KEVENC'
    print(c)
    cA = c.split("; ")
    print(cA)
    print(len(cA))
    for szo in cA:


        """if len(szo) < 4:
            print(szo.lower())
        else:
            print(szo)"""
        

        if len(szo) < 4:
            szo = szo.lower()
        print(szo)
    print()
    d = "   elment a csiga               az    erdobe     \n "
    print(d.strip())
    print(len(d.strip()))
    print(d.lstrip())
    print(len(d.lstrip()))
    print(d.rstrip())
    print(len(d.rstrip()))
    e = ["egy darab szo", "ami amugy", "hazugsag mert", "az elobb ketto szo volt"]
    print()
    print(e)
    print(" - ".join(e))


if (__name__ == '__main__'):
    main()