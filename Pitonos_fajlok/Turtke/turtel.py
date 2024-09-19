import turtle
import os
import rajzok

def menu():
    os.system("cls")
    print("Teknőc: \n 1.) Szív \n 2.) Kocka \n 3.) Kör \n 4.) Hatszög \n 0.) Kilépés")
    
def main():
    c = ""
    pen = turtle.Turtle()
    while(c != "0"):
        menu()
        c = input("---> ")
        try:
            if c == "1":
                rajzok.sziv(pen)
            if c == "2":
                rajzok.kocka(pen)
            if c == "3":
                rajzok.kor(pen)
            if c == "4":
                rajzok.hatszog(pen)
        except:
            pass


if __name__ == "__main__":
    main()
