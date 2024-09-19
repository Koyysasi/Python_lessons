def main():
    a = "menostring"

    print(a[0:2]) # 0-tol 2. indexig
    print(a[4:10]) # 4.-től a 10-ig
    print(a[4:]) # 4-től a végéig
    print(a[:4]) # elejétől a 4.-ig
    print(a[::])
    print(a[9:0:-1]+a[0])
    print()
    print(a)
    print(reverse(a))
    print(ord('a'))
    print(chr(98))
    b = "abcdefghijklmnopqrstuvwxyz"
    print(caesar(b, 5))

def reverse(a):
    # return a[len(a)-1:0:-1]+a[0]
    t = ""
    for i in range(len(a)-1, -1, -1):
        t += a[i]
    return t
    
def caesar(s, c):
    t = ""
    for i in s:
        if ord(i)+c > 122:
            t += chr(97+(122-ord(i)))
        elif ord(i)+c < 97:
            t += chr(122-(ord(i)-97))
        else:
            t += chr(ord(i)+c)
    return t

if __name__ == '__main__':
    main()