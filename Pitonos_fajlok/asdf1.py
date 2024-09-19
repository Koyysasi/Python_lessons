import os
import time

def main():
    s = "Boti egy nagy rakás kedves ember."
    for i in range(0,len(s)):
        y = i+5
        print(s[i:y])
        time.sleep(0.1)
        os.system('cls')

if __name__ == '__main__':
    main()