from os import system as cmd

# tuple - rendezett 1-es, rendezett pár, rendezett hármas, stb.

cmd("cls")


my_tup1 = (1,)
my_tuple = (1, 2, 3)

print(my_tuple)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.append(4)
cmd("cls")
#print(hex(id(list1)))

list2 = [1, 2, 3]

"""for i in range(100):
    print(len(list2) + i)
    list1.append(i)"""


print(list2)


mytuple2 = tuple(list2)
l = list(mytuple2)
l[0] = -1
mytuple2 = tuple(l)

mytuple2 = mytuple2[::-1]

for element in mytuple2:
    print(element)


print("==========")
a = [1, 2, 3]
print(len(a))
del a 

a = (1, 2, 3)
b = (1, 2, 3)

print(a is b)
