import turtle as t

def is_prime(p):
	prime = True
	for ind in range(2,p//2+1):
		if p % ind == 0:
			prime = False
			break
	return prime

"""try:
	brick = int(input("Hány téglád van? -> "))
except TypeError:
	brick = int(input("Számot adj meg! -> "))

height = 0

while brick > 0:
	if brick >= height+1:
		height += 1
		brick -= height
	else:
		break


print(f"A piramisod {height} magas")
print(f"{brick} db tégla maradt")

for i in range(height):
	print((height-i+1)*"  "+(i+1)*"[Br]")"""

def teglalap(m, sz):
	print("┏"+"───"*(sz-2)+"┓")
	for i in range(m-2):
		print("┃"+"   "*(sz-2)+"┃")
	print("┗"+"───"*(sz-2)+"┛")

teglalap(5,5)


def draw():
	t.tracer(0,0)
	limit = 10000
	count = 1
	row = 0
	t.penup()
	font = ('arial', 5, '')
	while count < limit:
		for deg in [0, 90, 180, 270]:
			if deg in [0, 180]:
				move = font[1]*3
				row+=1
			else:
				move = 8
			t.seth(deg)
			for ind in range(row):
				t.forward(move)
				if is_prime(count):
					t.dot(3)
					t.write(f"{count:4}",font=font)
				count+=1
	t.update()
	t.exitonclick()

draw()
