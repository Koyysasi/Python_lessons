from random import randint as poloska

list = [1, 2, 3]
itered_list = iter(list)
print(next(itered_list))
print(next(itered_list))
print(next(itered_list))

"""for i in range(5):
	# print(i)
	pass

for i in list:
	# print(i)
	pass"""


def next_sqr():
	k = 1
	while True:
		yield k**k
		k += 1


sqr_iter = iter(next_sqr())
print(sqr_iter.__iter__())


def print_even(list):
	for i in list:
		if i % 2 == 0:
			yield i

l = []
for i in range(100):
	l.append(poloska(0, 100))
print(l)


def test():
	yield 1
print(type(test))


for i in print_even(l):
	print(i)