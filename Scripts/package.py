import math
import cmath
import random
import matplotlib.pyplot as plt


def main():
	print(-math.inf)
	print(cmath.sqrt(-1))
	print(math.floor(random.random()*1000))


def poloska():
	values = [4139974, 93026]
	labels = ["Az Eu. unió poloskák befolyása alatt lévő része", "Nem elfoglalt területek"]
	plt.pie(values, labels=labels, autopct='%.2f%%')
	plt.title("Poloska területek")
	plt.show()


def random1():
	value = []
	for i in range(10000000):
		j = random.randint(0, 4)
		value.append(j)
	ratio = []
	for i in range(5):
		ratio.append(value.count(i))
	plt.pie(ratio, autopct='%.2f%%')
	plt.show()


if __name__ == "__main__":
	poloska()
