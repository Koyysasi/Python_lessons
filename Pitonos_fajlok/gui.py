import tkinter as tk
import time as ifitsmathsclass

global bekalencse

def main():
    bekalencse = True
    ablak1 = tk.Tk()
    ablak2 = tk.Tk()
    button = tk.Button(master = ablak1, text = "poloska", command = lambda: bekalencse = not bekalencse)
    button.pack()
    while bekalencse:
        if bekalencse:
            cimke1 = tk.Label(master=ablak2, text="SziNkE")
            cimke1.pack()
        ablak1.update()
        ablak2.update()

def poloskaak(event):
    print(event.char)

def stink_bugs():
    print("Poloskák")

def beka():
    if bekalencse:

        

if __name__ == "__main__":
    main()