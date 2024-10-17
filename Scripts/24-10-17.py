from typing import TypeAlias, TypeVar, Any
import math
import os
import time

Matrix: TypeAlias = list[list[Any]]

matrix: Matrix = [['1', 2], ["poloska", True], [[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]], [complex(1, 10)], frozenset([1, 2, 3]), bytes("01010101", "UTF-8")]

#print(matrix)

#print(matrix[0])

#print(matrix[-1])

#print(matrix[2])

def create_matrix_1():
	mx1 = []
	for i in range(4):
		mx1.append([])
		for j in range(3):
			mx1[i].append(j)


def create_matrix_2():
	mx1 = []
	for i in range(3):
		mx1.append([])
		for j in range(4):
			mx1[i].append(j)


def print_matrix_by_row(m: Matrix):
	for i in m:
		print(i)


def create_matrix(n: int, m: int, o: int = 0) -> Matrix:
	mx1 = []
	for i in range(n):
		mx1.append([])
		for j in range(m):
			mx1[i].append([])
			for k in range(o):
				mx1[i][j].append(0)
	return mx1


matrix = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]
]
def index(i: int, mx: Matrix) -> Any:
	rows = len(mx)
	print(rows)
	columns = len(mx[0])

	row = math.floor(i/rows)
	print(row)
	index = i-(row)*columns
	print(index)
	return mx[row][index]

print(index(6, matrix))

mx2 = [
	["a", "b", "c"],
	["1", "a", "a"],
	["a", "a", "a"]
]

mx2.sort()
#print_matrix_by_row(mx2)


#print_matrix_by_row(create_matrix(2,2, 2))
while True:
	try:
		num = int(input("Írj be egy számot -> "))
		# Ha itt van kagi akkor ez itt eltöri magát
	except ValueError:
		print("Ezt elbaltáztad...")
		time.sleep(1)
		os.system("cls")