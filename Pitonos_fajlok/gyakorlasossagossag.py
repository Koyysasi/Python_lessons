import os
import time

def main():
    os.system("cls")
    s = "Mondjá' valamit! kumpi csak {price:.2f}"
    print(s.format(price = 10.3274572572735))

    s2 = "Középre igazított {:^42} szöveg"
    print(s2.format(input("Mondjá' valamit! > ")))
    print(s2.format("poloooooooooooooooooooooooooooooooooos"))

    s3 = "Balra {:<20} igazított"
    print(s3.format(input("Mondjá' valamit! > ")))

    s4 = "Jobbra {:>20} igazított"
    print(s4.format(input("Mondjá' valamit! > ")))

    s5 = "Középre {:>10}"
    print(s5.format("alma")+"{:<10} igazított".format(""))

    s6 = "Végtelende végtelen {:,}"
    print(s6.format(10000000000))

    halmaz = {2, 4, 6, 8, 10}
    halmaz2 = {1, 3, 5, 7, 9}
    halmaz3 = {1, 2, 6, 8, 9}
    print(halmaz, halmaz2, halmaz3)
    print(halmaz.intersection(halmaz2))

    time.sleep(3.0)
    for i in range(10): print("")
    ans = ""
    while ans != "y":
        ans = input("TOVÁBB? ( y / n ) >>> ")
        if ans == "n":
            ans2 = input("KILÉPÉS? ( y / n ) >>> ")
            if ans2 == "y":
                break
        else: pass
    for i in range(2):
        print("-")
        time.sleep(0.2)
        os.system("cls")
        print("\ ")
        time.sleep(0.2)
        os.system("cls")
        print("|")
        time.sleep(0.2)
        os.system("cls")
        print("/")
        time.sleep(0.2)
        os.system("cls")

    resztvevok = {"Alma", "béka", "cmmm"}
    resztvevokId = []

    for i in resztvevok:
        a = 0
        for j in i:
            a += ord(j.lower if j.isupper() else j.upper())
        print(a)
        resztvevokId.append(a)
    
def insertionSort(arr, arrId):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arrId[i]
        j = i - 1
        while j >= 0 and key < arrId[j]:
            arrId[j+1] = arrId[j]

if __name__ == "__main__":
    main()