import os
import random
import datetime
from timeit import default_timer as timer
import time

options = ["0", "1", "2", "3", "u", "U"]

def main():
    os.system("cls")
    print("C A S I O   B A T T L E   by koyysasi (V1)")
    print("-----")
    ans = ""
    while(ans != "0"):
        print("[0] Quit")
        print("[1] Start battle")
        ans = input(">>> ")
        if(str(ans) == "1"):
            battle()
            ans = ""
        os.system("cls")


def battle():
    player1 = input("Type the name of Player 1 >>> ")
    player2 = input("Type the name of Player 2 >>> ")
    if player1 == player2:
        input("Really? (¬_¬ )")
    player1hp = 10
    player2hp = 10
    player1ult = 1
    player2ult = 1
    draw = True
    while player1hp >= 0 and player2hp >= 0:
        os.system("cls")
        print(f"It's {player1}'s turn. ")
        print("-----")
        print("[0] Attack")
        print("[1] Heal")
        print("[2] Check")
        print("[3] Skip turn")
        if draw == True:
            print("[4] Draw")
        if player1ult == 1:
            print("[U] Ultimate (instantly deals 2 damage and heals 1 hp)")

        ans = input(">>> ")

        if str(ans) == "0":
            player2hp = fight(player1, player2hp, player2)

        elif str(ans) == "1":
            player1hp += heal(player1, player1hp)

        elif str(ans) == "2":
            print(f"{player1} checked {player2}! ")
            print(f"HP left: {player2hp}, ULT status: {"READY" if player2ult == 1 else "USED"} - Your ULT is {"READY" if player1ult == 1 else "USED"}")
            input("... ")

        elif str(ans) == "u" or str(ans) == "U":
            if player1ult == 1:
                input(f"{player1} is preparing a special attack... ")
                print(f"{player1} used their ULT! ")
                print(f"{player2} lost 2 HP!")
                print(f"{player1} recovered 1 HP! ")
                player1ult = 0
                player1hp += 1
                player2hp -= 2
                input("... ")
            else:
                print(f"{player1} tries to gather all of their power, but fails")
                print(f"{player1}'s ULT is USED")
                print("Nothing happens.")
                input("... ")

        elif str(ans) == "4" and draw == True:
            draw = drawfunc(player1, player2, player1hp, player2hp)

        elif ans not in options or str(ans) == "3":
            print(f"{player1} skipped their turn!")
            input("... ")

        # End of player 1's turn

        os.system("cls")
        print(f"It's {player2}'s turn. ")
        print("-----")
        print("[0] Attack")
        print("[1] Heal")
        print("[2] Check")
        print("[3] Skip turn")
        if draw == True:
            print("[4] Draw")
        if player2ult == 1:
            print("[U] Ultimate (instantly deals 2 damage and heals 1 hp)")
        ans = input(">>> ")
        
        if str(ans) == "0":
            player1hp = fight(player2, player1hp, player1)

        if str(ans) == "1":
            player2hp += heal(player2, player2hp)

        elif str(ans) == "2":
            print(f"{player2} checked {player1}! ")
            print(f"HP left: {player1hp}, ULT status: {"READY" if player1ult == 1 else "USED"} - Your ULT is {"READY" if player2ult == 1 else "USED"}")
            input("... ")

        elif str(ans) == "4" and draw == True:
            draw = drawfunc(player2, player1, player2hp, player1hp)

        elif str(ans) == "u" or str(ans) == "U":
            if player2ult == 1:
                input(f"{player2} is preparing a special attack... ")
                print(f"{player2} used their ULT! ")
                print(f"{player1} lost 2 HP!")
                print(f"{player2} recovered 1 HP! ")
                player2ult = 0
                player2hp += 1
                player1hp -= 2
                input("... ")
            else:
                print(f"{player2} tries to gather all of their power, but fails")
                print(f"{player2}'s ULT is USED")
                print("Nothing happens.")
                input("... ")

        elif ans not in options or str(ans) == "3":
            print(f"{player2} skipped their turn!")
            input("... ")
    if player1hp <= 0:
        os.system("cls")
        print(f"{player1} was defeated! ")
        print(f"{player2} wins!")
        print("-----")
        print("BATTLE SUMMARY")
        print(f"HP left for {player2}: {player2hp}")
        input("... ")
        quit()
    elif player2hp <= 0:
        os.system("cls")
        print(f"{player2} was defeated! ")
        print(f"{player1} wins!")
        print("-----")
        print("BATTLE SUMMARY")
        print(f"HP left for {player1}: {player1hp}")
        input("... ")
        quit()  
    else:
        os.system("cls")
        print("Wait, how did you do this??")
        print("-----")
        print("BATTLE SUMMARY")
        print("It looks like the developer messed this up... (please contact the dev)")


def fight(player, opphp, opponent):
    print(f"{player} attacks! ")
    print("Enter anything when you see NOW! ")
    rand = random.uniform(1.0, 5.0)
    round(rand, 2)
    time.sleep(rand)
    start = time.time()
    input("NOW! ")
    rtime = time.time() - start

    if rtime <= 0.2:
        print(f"{player}, you are either a robot or a cheater! ")
        print("Nothing happens.")
        input("... ")
        return opphp
    if rtime <= 0.35 and rtime > 0.2:
        print(f"{player} performed a critical hit! ")
        print(f"{opponent} lost 3 HP! ")
        if opphp < 0: 
            return 0
        opphp -= 3
        input("... ")
        return opphp
    elif rtime <= 0.4 and rtime > 0.2:
        print(f"{player} does a perfect hit! ")
        print(f"{opponent} lost 2 HP! ")
        if opphp < 0: 
            return 0
        opphp -= 2
        input("... ")
        return opphp
    elif rtime <= 0.5 and rtime > 0.2:
        print(f"{player} hits! ")
        print(f"{opponent} lost 1 HP! ")
        if opphp < 0: 
            return 0
        opphp -= 1
        input("... ")
        return opphp
    else:
        print(f"{player} missed! ")
        print("Nothing happens.")
        input("... ")
        return opphp



def heal(player, playerhp):
    input(f"{player} used heal! ")
    rand = random.randrange(1,4)
    print(f"{player} recovered {rand} HP! ")
    input("... ")
    os.system("cls")
    return rand

def drawfunc(player, opponent, playerhp, opponenthp):
    print(f"{player} is offering a draw! ")
    ans = ""
    while(ans != "y" or ans != "n"):
        ans = input(f"{opponent}, do you accept? ( y / n ) >>> ")
        if ans == "y":
            os.system("cls")
            print(f"{opponent} accepted! ")
            print("Nobody wins!")
            print("-----")
            print("BATTLE SUMMARY")
            print(f"HP left for {player}: {playerhp}, HP left for {opponent}: {opponenthp}")
            input("... ")
            quit()
        else:
            if playerhp >= opponenthp:
                print(f"{opponent} wants to fight! ")
                input("... ")
                return False
            elif playerhp <= opponenthp:
                print(f"{opponent} won't let you escape! ")
                input("... ")
                return False
        


if __name__ == "__main__":
    main()