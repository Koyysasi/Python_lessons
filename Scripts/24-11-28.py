

tup1 = (1,)

tupli = (1, 2, 3)

print(tupli)
print(type(tupli))
print(tupli[1])

# Tuple-hoz nem lehet értéket hozzáadni

it = range(5)

print(hex(id(it)))


a = [1, 2, 3]
tupli2 = tuple(a)
l = list(tupli2)
l[0] =-1
tupli2 = tuple(l) # felülírás


tupli2 = tupli2[::-1] # megfordítás [start_index:stop_index:step]


for element in tupli2:
	print(element)


a = [1, 2, 3]
print(len(a))
del a[2]
print(len(a))



