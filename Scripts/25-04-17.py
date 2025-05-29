def new_file():
	file = open("file.txt", "w+")
	file.write("Én vagyok betmen")
	file.seek(0)
	print(file.read())
	file.close()

new_file()

def letter_count(x):
	with open("file.txt", "r") as f:
		file = f.read()

	counter = 0
	for i in file:
		if i == x:
			counter+=1

	if x == " ":
		print(f"Ebben a fájlban {counter+1} szó van")
	else:
		print(f"Ebben a fájlban {counter} '{x}' van")

letter_count("e")

def list_file():
	l = ['szia\n', 'fish\n', 'cat\n', 'ice\n', 'banana\n', 'grape\n']
	with open("szia.txt", "w+") as f:
		f.writelines(l)
		f.seek(0)
		file = f.read()
	print(file)

list_file()

def ages():
	names = open("Assets/names.txt", "r")
	ages = open("Assets/ages.txt", "r")
	pairs = dict()
	l_names = names.readlines()
	l_ages = ages.readlines()

	for i in range(len(l_names)):
		pairs[l_names[i].strip()] = int(l_ages[i].strip())

	print(pairs)
	return pairs

def ages_2(pairs):
	with open("pairs.txt", "w+") as f:
		for k in pairs.keys():
			f.write(f"{k} -> {pairs[k]}\n")
		f.seek(0)
		print(f.read())

ages_2(ages())

def poem_words():
	file = open("Assets/poem.txt", "r", encoding="UTF-8")
	words = file.read().split()
	for i in words:
		if i != " ":
			print(i, end=",")
	file.close()

poem_words()