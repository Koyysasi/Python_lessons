import os
from random import randint as rand

def main():
    os.system("whoami")
    sajatFuggveny(os.system("whoami"))
    import sajat
    beka = sajat.SajatOsztaly()
    print(f"\t sajat.SajatOsztaly()")


def sajatFuggveny(parameter):
    return str(parameter)+"is a Niger"

if __name__ == "__main__":
    main()