import os
import datetime
import base64
import math
import random
def main():
    os.system("cls" if os.name == "nt" else "clear")
    """
    honapok = ["","Január", "Február", "Március",
               "Április", "Május", "Június",
               "Július", "Augusztus", "Szeptember",
               "Október", "November", "December"]
    ido = datetime.datetime.now()
    print(f"Ma {honapok[ido.month]} {ido.day}.-a van")
    print(f"Most {ido.hour} óra, {ido.minute} perc, {ido.second} másodperc van")
    dani = bytes(input("Kódolásra ítélt szöveg: ").encode("ascii"))
    print(f"Elkódoltam: {base64.b64encode(dani)}")
    dodo = bytes(input("Kódolásról felmentett szöveg: ").encode("ascii"))
    print(f"Dekódoltam: {base64.b64decode(dodo)}")
    """
    szamok = {}
    min = 1
    max = 200
    s = 50000
    """
    print(szamok)
    szamok.update({0:15})
    print(szamok)
    """
    for i in range(min,max+1):
        szamok.update({i:0})
    print(szamok)
    for _ in range(s):
        v = random.randrange(min,max+1)
        szamok[v] += 1
    print(szamok)
    o = 0
    oN = 0
    e = list(szamok.items())
    for i in range(len(e)):
        o += e[i][0]*e[i][1]
        oN += e[i][1]
    print(f"o/oN: {o/oN}")

if __name__ == "__main__":
    main()