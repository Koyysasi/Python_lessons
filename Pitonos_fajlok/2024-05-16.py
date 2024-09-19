from random import randint as rng

def main():
    randomnum = [rng(1,100) for i in range(50)]
    randomnum.sort()
    print("Random számok: \n")
    [print(i, end=", ") for i in randomnum]
    print("")

    nemduplak = [i for i in randomnum if randomnum.count(i) == 1]
    print("Random számok duplák nélkül: \n")
    for i in randomnum:
        if i not in nemduplak:
            nemduplak.append(i)
    print(nemduplak)

    print("\nRandom számok 50-ig: ")
    for i in randomnum:
        if i>50:
            break
        print(i, end=", ")

    print("Páratlan: ")
    for i in randomnum:
        if i % 2 != 0:
            print(i, end=", ")

    for i in randomnum:
        if i % 2 == 0:
            continue
        print(i, end=", ")

    for i in range(10):
        if 7 > i > 3:
            continue
        print(i, end=", ")
        

def names():
    list = ["pita", "bela", "paraszt", "dr. polos", "sir pityoka", "vityus", "szintjáró pítör", "gyúró feri", "orbitális vityka bácsi", "német pítör", "zajos-márkus pál", "húsvét gerely"]

    print("\nfor i in list")
    for i in list:
        print(i, end=" ")

    print("\nfor i in range(len(list))")
    for i in range(len(list)):
        print(list[i], end=" ")

    print("\nwhile i < len(list)")
    i = 0
    while i < len(list):
        print(list[i], end=" ")
        i+=1

    print("\n Csak 9 vagy annál rövidebb nevű figurák")
    for i in list:
        if len(i) <= 9:
            print(i)

    print("\nMegoldás but shorter")
    [print(i, end=", ") for i in list if len(i) <= 9]

if __name__ == "__main__":
    main()