from typing import TypeAlias, TypeVar, Any
import os
os.system("cls")


Matrix: TypeAlias = list[list[Any]]

matrix = [['1', 2],
          [3, True]]

"""print(matrix, "\n--------------------\n")
print(matrix[0], "\n------------------------\n")
print(matrix[-1])"""

"""print(matrix[0][1])
row: list[Any] = matrix[0]
element: Any = row[0]"""

def create_matrix_1():
    mx1 = []
    for i in range(4):
        mx1.append([])
        for j in range(3):
            mx1[i].append(j)
    return mx1

def print_matrix_by_row(m: Matrix):
    for i in m:
        print(i)




def create_matrix(n: int, m: int) -> Matrix:
    mx1 = []
    for i in range(n):
        mx1.append([])
        for j in range(m):
            mx1[i].append(j)
    return mx1


mx = create_matrix(3, 7)
mx[2][0] = "a tzsaf"


mx1 = [[5, 2, 4],
       [5, 5, 1],
       [6, 2, 5]]
mx1.sort()
print_matrix_by_row(mx1)

print("\n---------------------\n")
for i in mx1:
    i.sort()
print_matrix_by_row(mx1)

print("\nohio\n")

def create_matrix_labeled(n: int, m: int) -> Matrix:
    mx1 = []
    counter = 0
    for i in range(n):
        mx1.append([])
        for j in range(m):
            mx1[i].append(counter)
            counter += 1
            
    return mx1

print_matrix_by_row(create_matrix_labeled(3,5))

def get_element_by_one_index(mx: Matrix, ind: int) ->Any:
    rows = len(mx)
    columns = len(mx[0])
    return mx[ind // columns][ind % columns]

mx2 = create_matrix_labeled(3, 5)

print("\nOHIO\n")
for i in range(15):
    print(get_element_by_one_index(mx2,i), i)