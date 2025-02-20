class newException(Exception):
	def __init__(self, message):
		self.message = message

"""if number.isdecimal():
	print(f"A szám fele {int(number) / 2}")
else:
	print(":/")"""

"""try:
	number = input("Kérek egy számot -> ")
	print(f"A szám fele {int(number) / 2}")
except:
	print(":/")"""

"""try:
	number = int(input("Szám -> "))
	print(f"A szám reciproka {1/number}")
except ValueError:
	print("HIBA: Nem egy szám")
except ZeroDivisionError:
	print("HIBA: 0 reciproka nem definiált")
except:
	print("HIBA: git gud")"""

"""
number = input("Szám -> ")
if number > 0:
	print("A szám pozitív")
elif number < 0:
	print("A szám negatív")
else:
	print("A szám nulla")"""


def division(a, b):
	try:
		c = a / b
		print(f"A két szám hányadosa {c}")
	except TypeError:
		print("HIBA: Nem szám")
	except ZeroDivisionError:
		print("HIBA: Nullával nem lehet osztani")
	else:
		print(":/")


division(1, 2)

try:
	f = open("text.txt")
	try:
		f.write("kacsa")
	except:
		print("Nem lehet írni a fájlba")
	finally:
		f.close()
except:
	print("A fájlt nem lehet megnyitni")

myList = [1, 2, 3, "banán", 5, 6, "alma", 8]
value = 0
numbers = 0
for i in range(0, len(myList)):
	try:
		value += myList[i]
	except TypeError:
		print(f"{myList[i]}. elem nem megfelelő típusú")

num2 = input("Adj meg egy számot -> ")
if num2.isdecimal():
	num2 += 5
else:
	raise Exception("Ez nem egy szám")
