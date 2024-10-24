
import matplotlib.pyplot as plt
import numpy as np

def cube_plot():
	axes = [5, 5, 5]
	data = np.ones(axes)
	alpha = 0.7
	colors = np.empty(axes + [4])
	#            R  G  B  átt.
	colors[0] = [1, 0, 0, alpha]
	colors[1] = [0, 1, 0, alpha]
	colors[2] = [0, 0, 1, alpha]
	colors[3] = [1, 1, 0, alpha]
	colors[4] = [1, 1, 1, alpha]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")
	ax.voxels(data, facecolors=colors, edgecolors="grey")
	ax.set_title("Színes kocka")
	plt.show()

cube_plot()


exit()

# list = [expression iterable conditions]
# statement: csinál vmit (if, while, a = 3)
# expression: kiértékelhető, értéke van (3, main(), True, "a".endswith("a"), 3**2)
list1 = [x for x in range(10)]
list2 = [x for x in range(10) if x % 2 == 0]
list3 = [0 for x in range(10) if x % 2 == 0]
list4 = [(x+1)**2 for x in range(10)]

print(list1, f"\n", list2, f"\n", list3, f"\n", list4)

def print_matrix_by_row(mx):
	for row in mx:
		print(row)


matrix1 = [[i for i in range(5)] for _ in range(5)]

print_matrix_by_row(matrix1)


fruits = ["apple", "banana", "orange", "peach", "pear"]

filtered = [f for f in fruits if f.count('b') >= 1]

print(filtered)


exit()


try:
	global user_input
	user_input = int(input("Adj meg egy egész számot: "))
except ValueError:
	print("NEIN")


matrix = [
	[1,2],
	[3,4]
]

print(matrix[0][1])


matrix2 = []


for i in range(5):
	matrix2.append(i)
	for j in range(5):
		matrix2[i].append(0)

