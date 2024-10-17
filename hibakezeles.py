from time import sleep as wait
while True:
    try:
        num = int(input("Írj be egy számot: "))
        print(num)
        break
    except ValueError:
        print("NEM JÓ SZÁM")
    except KeyboardInterrupt:
        print("kilépés")
        wait(2)
        exit()

#ValueError