"""kord = {'x':10, 'y':20, 'z':30}

for key, value in kord.items():
	print(key, " - ", value)

nums = {1:1,2:2,3:4,4:3,5:5,6:6}

for key, value in kord.items():
	if value % 2 == 0:
		print(key, " - ", value)

dict = dict()

for x in range(1, int(input("Numbers --> "))+1):
	dict[x] = x**2

print(dict)"""

"""dict2 = {'adat1' : 1, 'adat2' : 2, 'adat3' : 3, 'adat4' : 6}
result = 1

for x in dict2.keys():
	result = result * dict2[x]

print(result)"""

"""kord2 = {'x':768, 'y':432, 'z':874}

print(f"Min: {min(kord2.values())}")
print(f"Max: {max(kord2.values())}")

dict3 = {1 : [1,2], 2: [3,4], 3 : [5,6]}

a, b, c = dict3.values()

for i in a:
	for j in b:
		for z in c:
			print(i+j+z)

print(a,b,c)

"""

pepols = dict()

"""while True:
	pepol = input("Mi a neved: ")
	if pepol == '':
		break
	else:
		peopel = []
		age = int(input(f"Hány éves {pepol}: "))
		gender = input(f"Milyen nemként azonosítja magát {pepol}: ")
		job = input("Munka: ")

		list = [age, gender, job]
		for i in list:
			peopel.append(i)

		pepols[pepol] = peopel

for ember in pepols.keys():
	print(ember, " - ", pepols[ember])
	"""

dict4 = dict()
print("üres" if len(dict4) == 0 else "van benne valami")


import pprint as pp

student_data = {
	'id1':{'name':['Sara'], 'class':['V'], 'subject_integration':['english, math, science']},
	'id2':{'name':['David'], 'class':['V'], 'subject_integration':['english, math, science']},
	'id3':{'name':['Sara'], 'class':['V'], 'subject_integration':['english, math, science']},
	'id4':{'name':['Surya'], 'class':['V'], 'subject_integration':['english, math, science']}
}

pp.pprint(student_data)

result = dict()

for key, value in student_data.items():
	if value not in result.values():
		result[key] = value

pp.pprint(result)

def kereses_a_listaban(lista, szam):
	found = []

	for i in range(len(lista)):
		if szam == lista[i]:
			found.append(i)
	if len(found) == 1:
		return found[0]
	elif len(found) == 0:
		return None
	else:
		return found

