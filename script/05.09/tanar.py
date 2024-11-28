import os
os.system("cls")

'''
Kalandjáték pythonban

Szövegalapú játék lesz
RPG- stílusú
Akár lehet saját sztorit is írni
Legalább egy pályát elkészítünk

'''

inevntory_size = 20
inventory = []
inventory_stats = []
armor = ["Cipő", "Nadrág", "Ing", ""]
armor_stats = [1, 1, 1, 0]

health = 100
damage = 10

def main_story():
    print("""Történetünk a sötét középkorban játszódik, ahol mi egy 
    lovagot irányítunk, akit Ferdinandnak hívnak.
    A játék lényege, hogy a királynő megbízásából visszaszerezzük a 
    korornaékszereket, amit titokzatos tolvajok elloptak. 
    Kalandunk során sok veszéllyel és rejtállyel találkozunk.
    """)

def level_1():
    print("Reggel 8 óra van")
    print("Fort valahol vagyunk, ahol éppen most keltünk fel.")

    equipement_inside = ["Kard", "Pajzs", "Kenyér", "Víz", "Térkép"]

    got_everythong = False
    while (not got_everythong):
        print()
        print(inventory)
        print(inventory_stats)
        print(equipement_inside)
        print(got_everythong)
        print()

        answer = int(input("Add meg, hogy melyik szobába szeretnél belépni (1-3): "))
        # 1. szoba/////////////////////////////////////////////////////////////
        if answer == 1:
            print("Ó ez a kard!!! Még édesapámtól kaptam.")
            print("Nyomd meg az 'F' gombot, hogy kivedd a szekrényből a kardot")
            print("Nyomd meg az 'X' gombot, hogy kilépj a szobából")
            action = input()
            if action.upper() == "F":
                if "Kard" in equipement_inside:
                    inventory.append("Kard")
                    inventory_stats.append(7)

                    equipement_inside.remove("Kard")
        # 2. szoba////////////////////////////////////////////////////////////////
        if answer == 2:
            print("Erre a térképre még szükségem lehet, "
                  "de ha már itt vagyok  apajzsot is magammal viszem")
            print("Nyomd meg az 'F' gombot, hogy fölvedd a tárgyakat")
            print("Nyomd meg az 'X' gombot, hogy kilépj a szobából")
            action = input()
            if action.upper() == "F":
                if "Pajzs" in equipement_inside and "Térkép" in equipement_inside:
                    inventory.append("Pajzs")
                    inventory.append("Térkép")
                    inventory_stats.append(4)
                    inventory_stats.append(1)

                    equipement_inside.remove("Pajzs")
                    equipement_inside.remove("Térkép")
        # 3. szoba////////////////////////////////////////////////////////////////
        if answer == 3:
            print("Út közben megéhezhetek, ezekre még szükség lehet")
            print("Nyomd meg az 'F' gombot, hogy fölvedd a tárgyakat")
            print("Nyomd meg az 'X' gombot, hogy kilépj a szobából")
            action = input()
            if action.upper() == "F":
                if "Kenyér" in equipement_inside and "Víz" in equipement_inside:
                    inventory.append("Kenyér")
                    inventory.append("Víz")
                    inventory_stats.append(1)
                    inventory_stats.append(2)

                    equipement_inside.remove("Kenyér")
                    equipement_inside.remove("Víz")
        # meg van-e minden?
        if len( equipement_inside ) == 0:
            got_everythong = True

def level_2():
    print("ELindultunk az útra, aztán megálltunk megpihenni egy fogadóban, "
          "ahol ráismertünk az egyik tolvajra. Próbáljuk meg elkapni,"
          " és megszerezni az információt.")
    print("De vigyázz!!! Fegyver van nálik, próbálj meg lopakodni!!")

    print("1. Lopakodva követni a rablót a szobájába")
    print("2. Megkérdezzük a fogadóban lévő embereket")
    print("3. mi magunk csikarjuk ki belőle az információt (veszélyes!!!!)")
    answer = int( input() )
    if answer == 1:
        print("Követtük a szobáig, ahol a kulcslyukon keresztül láttuk, ahogy egy titkos dokumentumot olvas.")
    elif answer == 2:
        print("Ő mégsem a rablókhoz tartozik, viszont kapcsolatban áll velük. Talán tudhat rólik valamit")
    elif answer == 3:
        if "Kard" in inventory:
            print("Megijesztettük az embert, aki fontos infókat árult el.")
            print("Megtudtuk, hogy a rablók bázisa 2 megyével odébb van egy titkos barlangban.")
        else:
            print("Elmemekült az ember, semmit nem tudtunk meg.")
def main():
    main_story()
    level_1()
    level_2()

if __name__ == "__main__":
    main()








