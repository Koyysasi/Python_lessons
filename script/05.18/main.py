import os
from random import randint
os.system("cls")

def nevek():
    lista = ["Dani", "krisz", "Shintago", "Gyuri", "Vityóka", "Levi", "Német Peti", "Húsvét Gergely"]

    for i in lista:
        print(i)
    
    for i in range(len(lista)):
        print(lista[i])
    
    i = 0
    while i < len(lista):
        print(lista[i], end=" ")
        i += 1
    
    print("\n[print(i, end=" ") for i in lista]")
    [print(i, end=" ") for i in lista]

    
    print("\n\ncsak 4 vagy annál rövidebb nevű emberek")
    for i in lista:
        if len(i) <= 4:
            print(i, end=" ")
    
    print("\nRövidebb módszer:")
    [print(i, end=" ") for i in lista if len(i) <= 4]

def randomok():
    
    randomszamok = [randint(1,100) for i in range(500)]
    randomszamok.sort()
    print("\n\nrandom számok")
    [print(i, end=" ") for i in randomszamok]
    nemduplak = [i for i in randomszamok if randomszamok.count(i) == 1]

    nemduplak2 = []
    for i in randomszamok:
        if i not in nemduplak2:
            nemduplak2.append(i)
    print("\nrandom számok duplák nélkül")
    [print(i, end=" ") for i in nemduplak2]

    print("\n\n randomszámok 50-ig")
    for i in randomszamok:
        if i > 50:
            break
        print(i, end=" ")


    for i in randomszamok:
        if i % 2 != 0:
            print(i, end= " ")

    for i in randomszamok:
        if i % 2 == 0:
            continue
        print(i, end= " ")

    print("\n\n Bemutatás indexel: ")
    for i in range(10):
        if 7 > i > 3:
            continue
        print(i, end= " ")


def main():
    randomok()
if __name__ == "__main__":
    main()