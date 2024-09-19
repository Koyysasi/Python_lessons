import os
import rajzok

def menu():
    os.system("cls")
    print("Teknőc: \n 1.) Szív \n 2.) Kocka \n 3.) Kör \n 4.) Hatszög \n 0.) Kilépés")
    
def main():
    c = ""
    while(c != "0"):
        menu()
        c = input("---> ")


if __name__ == "__main__":
    main()