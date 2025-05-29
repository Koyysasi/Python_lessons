def star_end_str(string, length):
	if len(string) < length*2:
		return string
	else:
		return string[:length] + string[-length:]

print(star_end_str("sziatepoloska", 3))

def replace_all_letters(string, fromLetter, toLetter):
	newStr = str()
	for i in string:
		if i.lower() == fromLetter.lower():
			newStr += toLetter
		else:
			newStr += i
	return newStr

print(replace_all_letters("POLOSKA", "O", "i"))

def first_repeated(string):
	checkedLetters = []
	for i in string:
		if i in checkedLetters:
			return i
		else:
			checkedLetters.append(i)

def matrix_to_list(matrix):
	newlist = []
	for x in matrix:
		for y in x:
			newlist.append(y)
	return newlist

szigMagyarPeter = {"Piros": 1, "Zöld": 4, "Kék": 2, "Fekete": 3, "Fehér": 5}

def sort_dictionary(dic, reverse=False):
	return dict(sorted(dic.items(), key=lambda x: x[1]), reverse=reverse)


mylist = [x for x in range(1,11)]

def drop_3rd_chars():
	temp = 0
	print(mylist)
	for i in range(len(mylist)):
		if i % 3 == 0 and i > 0:
			print(i)
			mylist.pop(i-1-temp)
			temp += 1
	print(mylist)

def drop_3rd_chars_2_0():
	remove = []
	for i in range(len(mylist)):
		if i % 3 == 0 and i > 0:
			remove.append(mylist[i])
	for i in remove:
		mylist.remove(i)


drop_3rd_chars_2_0()
print(mylist)




