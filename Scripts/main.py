def recursive(num):
    print(num)
    if num > 0:
        num -= 1
        recursive(num)


def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)


def fact2(n, result=1):
    if n <= 0:
        return result
    else:
        return fact2(n-1, result * n)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def mathstuff(n, value=0):
    if n <= 0:
        return value
    else:
        return mathstuff(n-1, value+(1/n))


def harm(n):
    if n <= 1:
        return 1
    else:
        return 1 / n + (harm(n-1))


def exponent(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return exponent(a, b-1) * a


def listsum(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + listsum(lista[1:])


if __name__ == "__main__":
    print(listsum([1, 2, 3]))
