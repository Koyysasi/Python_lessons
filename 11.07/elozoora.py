import numpy as np
import matplotlib.pyplot as plt


# KeyboardInterrupt
def read_int():
    while True:
        try:
            return int(input("Irj be egy egesz szamot: "))
        except ValueError:
            print("Hibe! Probald ujra!")
        finally:
            print("Ez mindig lefut")


def print_matrix_by_row(mx):
    for row in mx:
        print(row)

# statement: csinál valamit: if ... while(), except: ... , a = 3
# expression: kiértékelhető, értéke van: 3, 3 + 1, 2 ** 3, True, "a".endswith('a')



# list = [expression iterable conditions]

list1 = [x for x in range(10)]
print(list1)

list2 = [x for x in range(10) if x % 2 == 0]
print(list2)

list3 = [0 for x in range(10) if x % 2 == 0]
print(list3)

list4 = [(x + 1) ** 2 for x in range(10)]
print(list4)

matrix1 = [[i for i in range(4)] for _ in range(3)]


print_matrix_by_row(matrix1)

fruits = ["apple","banana","orange","peach"]

filtered = [f for f in fruits if f.count('a') >= 1]

matrix2 = [[[3, 4, 5], [6, 7, 8]]]
print(matrix2[0][1][1])

print(filtered)


def cube_plot():
    axes = [5, 5, 5]
    data = np.ones(axes)
    alpha = 0.7
    colors = np.empty(axes + [4])
    #            R  G  B  áttetszőség
    colors[0] = [1, 0, 0, alpha]
    colors[0][1] = [0, 1, 1, alpha]
    colors[1] = [0, 1, 0, alpha]
    colors[2] = [0, 0, 1, alpha]
    colors[3] = [1, 1, 0, alpha]
    colors[4] = [1, 1, 1, alpha]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.voxels(data, facecolors=colors, edgecolors='grey')

    ax.set_title("Színes kocka")
    plt.show()

cube_plot()



# ValueError

exit()
matrix = [[1, 2],
          [3, 4]]
print(matrix[0][1])

matrix2 = []
for i in range(5):
    matrix2.append([])
    for j in range(3):
        matrix2[i].append(0)
for row in matrix2:
    print(row)









