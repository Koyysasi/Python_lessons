from typing import *
from time import sleep as varj
from os import system as terminal
import random

terminal("clear")

def increment( x: int) -> int:
    return x + 1

def id_int(x: int) -> int:
    return x

def add_first_two(l: list[Union[int, float]]) -> Union[int, float]:
    return l[0] + l[1]

T = TypeVar("T")
def id(x: T) -> T:
    return x

point: TypeAlias = tuple[int, int]


def is_origo(point: point) -> bool:
    return point[0] == 0 and point[1] == 0


#print(id_int(2))
#print(id_int(2.0))
#print(id_int("alma"))


def listak():
    list = [1, 2, 3]
    itered_List = iter(list)
    print(next(itered_List))
    print(next(itered_List))
    print(next(itered_List))
    print("-----")
    print("-----")
    for i in range(5):
        print(i)
    print("-----")
    for i in list:
        print(i)


def next_sqr():
    k = 1
    while True:
        yield k * k
        k += 1
sqr_iter = iter(next_sqr())
print(sqr_iter.__iter__())
print("end")
for i in sqr_iter:
    if i > 100:
        break
    print(i)


def filter_even(list):
    for i in list:
        if i % 2 == 0:
            yield i

l = []
for i in range(100):
    l.append(random.randint(0, 100))
print(l)

for i in filter_even(l):
    print(i)


def test_gen1():
    return 1
def test_gen2():
    yield 2
print(type(test_gen1))
    