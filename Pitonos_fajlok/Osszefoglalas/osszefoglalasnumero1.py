def main():
    print("INPUT:")
    a = input(">>> ")
    print("OUTPUT: ")
    print(a)
    print("VÁLTOZÓK = ADATTÍPUSOK")
    int = int(1)
    float = float(0.1)
    string = str("H e l l o W o r l d")
    bool = bool(True)
    print("EGÉSZ SZÁM" + str(int))
    print("TÖRTSZÁM " + str(float))
    print("SZTRING" + str(string))
    print("LOGIKAI" + str(bool))
    print("COMPLEXEBB ADATTÍPUSOK (GYŰjTEMÉNYEK)")
    tomb = [1, 2, 3, 4, 5, 6]
    list = list()
    set = set()
    tuple = tuple()
    dict = dict()
    list = ["Alma", 23, True, 1.25]
    set = {1, 2, 3}
    set2 = {3, 4, 5}
    dict = {"Alma": 315, "Körte": 500, "Csirke": 1500}
    print("Alap matematikai műveletek: "
          "\tÖSSZEADÁS: +\n"
          "\tKIVONÁS: -\n"
          "\tSZORZÁS: *\n"
          "\tOSZTÁS: /\n"
          "\tKEREKÍTETT OSZTÁS: //\n"
          "\tHATVÁNYOSÍTÁS: **\n")
    print("Alap logikai és bit operátorok: \n"
          "\t AND : and\n"
          "\t OR : or\n"
          "\t NOT : not\n"
          "\t XOR : xor\n"
          "\t BIT AND : &\n"
          "\t BIT OR : |\n"
          "\t BIT NOT : ~\n"
          "\t BIT XOR : ^\n"
          "\t BIT LEFT SHIFT : <<\n"
          "\t BIT RIGHT SHIFT : >>\n"
          )
    print("Szöveg függvények:\n"
          f"\tKarakterszám: count = {len(string)}\n"
          f"\tÜres karakterek törlése: strip = {string.strip()}\n"
          f"\tFeldarabolás: split(SEPARATOR) = {string.split(" ")}\n"
          f"\tMivel kezdődik: startswith(CHARACTER) = {string.startswith('a')}\n"
          f"\tMivel végződik: endswith(CHARACTER) = {string.endswith('a')}\n"
          f"\tKapitalizálás: capitalize = {string.capitalize()}\n"
          f"\tNagybetűsítés: upper = {string.upper()}\n"
          f"\tKisbetűsítés: lower = {string.lower()}\n"
          f"\tSzvapkész: swapcase = {string.swapcase()}\n"
          f"\tCsupa kisbetü: islower = {string.islower()}\n"
          f"\tCsupa nagybetű: isupper = {string.isupper()}\n"
          f"\tÖsszefűzés tömbből: join(TOMB) = {string.join(tomb)}\n"
          f"\tHány darab valami: count(CHARACTER) = {string.count('o')}\n")
    print("Lista függvények:\n")
    list.append("Brekeke")
    print(f"\tHozzáadás: append(ELEM)")
    list.remove("Brekeke")
    print(f"\tEltávolítás: remove(ELEM)")
    list2 = [1, 54, 513, 76, 35, -534, 0]
    list2.sort()
    print(f"\tRendezés: sort()")
    list.insert(3, "Brekekekekek")
    print(f"\tBeszúrás: insert(INDEX, ELEM)")
    print(f"\tHelykeresés: index(INDEX) = {list2.index(3)}")
    list2.reverse()
    print(f"\tVisszafelé: reverseí)")
    a = input("... ")

if __name__ == "__main__":
    main()


