def main():
    print("Hello world")

def inOneLine():
    pass


def IsItPrime(num: int) -> bool:
    # Program to check if a number is prime or not
    num = int(input("szam: "))

    for i in range(2,num // 2):
        if num <= 1:
            return False
        if num % i == 0:
            return False
    return True

def right_triangle(a, b, c = 3):
    	return (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2)

if __name__ == "__main__":
    IsItPrime(4)