import string

def isPrime(p):
	prime = True
	for i in range(2, p):
		if p % i == 0:
			prime = False
			break
	return prime

n = int(input("Adj meg egy számot: -> (int) "))
i = 2
primeList = []

while True:
	if isPrime(i):
		primeList.append(i)
	i+=1
	if i == n:
		break

print(primeList)

numero = int(input("Adj egy számot"))

while numero>1:
	if numero % 3 == 0:
		numero /= 3
	else:
		numero+=1
	print(numero)

i = 0
boolean = True
while boolean:
	print(i)
	i+=1
	if i == 50000:
		boolean = False

i = 0
list = list(range(10))

while i < len(list):
	print(list[i])
	i+=1

for i in list:
	print(i)

for i in range(len(list)):
	print(i)

my_string = input("Adj meg egy szöveget -->")
digits = 0
letters = 0

for char in my_string:
	if char.isdigit():
		digits += 1
	elif char.isalpha():
		letters += 1

print(digits, letters)


basket = {"apple" : 10, "banana" : 20, "orange" : 30}
fruit = input("Adj meg egy gyümölcst -> (str) ")
ind_ex = 0
for item in basket.keys():
	if item == fruit:
		print(f"A kosárban van {basket[item]} {item}")
		break
else:
	quantity = int(input(f"Add meg a mennyiségét a {fruit}-nek: \n"))
	basket[fruit] = quantity
	for item in basket:
		print(item, ":", basket[item], sep=" ")


rows = int(input("Add meg a sorok számát -> (int) "))
cols = int(input("Add meg az oszlopok számát -> (int) "))
myMatrix = [[0 for col in range(cols)] for row in range(rows)]

for i in range(len(myMatrix)):
	print(myMatrix[i])


def isValidPassword(password):
	length = False
	uppercase = False
	special_char = False
	digit = False
	lowercase = False

	for char in password:
		if char.isdigit():
			digit = True
		if char.isalpha():
			if char.islower():
				lowercase = True
			elif char.isupper():
				uppercase = True
		if string.punctuation.__contains__(char):
			special_char = True
	if 8 <= len(password) <= 20:
		length = True

	if length and special_char and digit and lowercase and uppercase:
		return "A jelszó valid"
	else:
		return "A jelszó nem valid"

print(isValidPassword("skibidiChonker235!"))