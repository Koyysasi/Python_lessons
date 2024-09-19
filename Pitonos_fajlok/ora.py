import os
import datetime
import base64
import math
import random

def main():
    """os.system("cls" if os.name == "nt" else "clear")
    time = datetime.datetime.now()
    months = ["Jaguár", "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
    print(f"Ma {months[time.month]} {time.day}. van.")
    kod = bytes(input("Kódolásra ítélt szöveg: ").encode("ascii"))
    print(f"Elkódoltam: {base64.b64encode(kod)}")
    dok = bytes(input("Kódolásról felmentett szöveg: ").encode("ascii"))
    print(f"Dekódoltam: {base64.b64decode(dok)}")
    
    print(math.factorial(5))
    print(random.randrange(0, 5))"""
    szamok = {}
    s = 500
    min = 1
    max = 5
    for i in range(min, max+1):
        szamok.update({i:1})
    
    for _ in range(s):
        v = random.randrange(min,max+1)
        if(szamok.get(v)):
            szamok[v] += 1
        else:
            szamok.update({v:1})
    print(szamok)


if __name__ == "__main__":
    main()