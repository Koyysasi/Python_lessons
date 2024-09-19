import os

loggedIn = False
data = []

def main():
    print("1.) Bejelentkezés")
    print("2.) Regisztráció")
    print("3.) Kilépés")
    options = ["1", "2", "3"]
    ans = input(">>> ")
    while(loggedIn == False):
        if(str(ans) == "1"):
            login()
        if(str(ans) == "2"):
            register()
        if(str(ans) == "3"):
            break
        ans = input(">>> ")

def login():
    if data == []:
        return
    f = input("Felhasználónév: ")
    j = input("Jelszó: ")
    print("Bejelentkezés")
    for i in data:
        if i[0] == f:
            if i[1] == j:
                print("Bejelentkezve! ")
        


def register():
    print("Regisztráció")
    print("Felhasználónév? ")
    username = ""
    while(username == ""):
        username = input(">>> ")
        username = str(username)
    print("Jelszó? ")
    password = ""
    while(password == ""):
        password = input(">>> ")
        password = str(password)
    list = [username, password]
    data.append(list)
    os.system("cls")
    print("Sikeres regisztráció! ")

if __name__ == "__main__":
    main()
