# 1. mód
import random

# r  ->> read: olvasás
# w ->> write: írás
# a ->> append: hozzáadás

adat = open("adat.txt", "rt")

sorok = adat.readlines()

adat.close()

# 2. mód

with open("adat.txt", "r") as adat2:
	sorok2 = adat2.readlines()

for i in sorok2:
	if i[4] != ";":
		print(i)
	elif i[6] != ";":
		print(i)

adatok = []
for i in range(len(sorok2)):
	temp = sorok2[i].strip().split(";")
	adatok.append(temp)

with open("file.txt", "w") as file:
	for i in adatok:
		file.write(f"Év: {i[0]} Osztály: {i[1]} Név: {i[2]}\n")

def ctrl_f(text, mode):
	if mode == 0:
		for i in adatok:
			if text.lower() in i[2].lower():
				print(i)
	elif mode == 1:
		for i in adatok:
			if text.lower() in i[0].lower():
				print(i)


"""for i in adatok:
	if i[0] == "2016":
		if i[1] == "b":
			print()"""


with open("number.txt", "w") as file:
	for i in range(100):
		file.write(f"{random.randint(0, 100)}\n")

with open("number.txt", "r") as sz:
	row = sz.readlines()
	print(sum(int(i) for i in row))
	print(sum(int(i) for i in row)/len(row))
	print(max(int(i) for i in row))
	print(min(int(i) for i in row))

