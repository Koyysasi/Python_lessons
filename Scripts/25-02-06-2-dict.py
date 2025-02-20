szotar = { "egy":1, "kettő":2, "három":3}
"""d = dict()

print(szotar.keys())
print(szotar.values())

kulcsok = szotar.keys()

for key in kulcsok:
	print(szotar[key])

print("----")

szotar["négy"] = 4
print(szotar["négy"])

print("----")

for elem in szotar.keys():
	print(elem)

print("----")

for elem in szotar.values():
	print(elem)

print("----")

szotar.update({"kettő":6})

for elem in szotar.values():
	print(elem)

print("----")

del szotar["kettő"]
szotar.popitem() # random elem kiszedése
szotar.pop("kettő")"""

dict1 = {1: 'value1', 2: 'value2'}
dict2 = {3: 'value3', 4: 'value4'}
dict3 = {5: 'value5', 6: 'value6'}
dict4 = {7: 'value7', 8: 'value8'}

dict5 = dict()

for szotar in (dict1,dict2,dict3,dict4):
	dict5.update(szotar)

print(dict5)

tanulok = dict()

while not len(tanulok) == 5:
	nev = input("Input. How would you make it move it? ")
	age = input("Hi Irish Roy.")
	if nev not in tanulok:
		tanulok[nev] = age
	else:
		tanulok.update({nev:age})

while not len(tanulok) == 5:
	nev = input("Input. How would you make it move it? ")
	score = input("Otherwise, how is it to eat Maci Vegas to go?")
	if nev not in tanulok:
		tanulok[nev] = score
	else:
		tanulok[nev] += score

print(szotar.items())

for i, j in szotar.items():
	print(i, " - ", j)


