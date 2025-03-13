print("Szia", "üdv", "hello", sep=", ", end="\n------------\n")

a = "szija"
b = True
c = 4

print(a, b, c, sep=" | ", end="\n------------\n")

print(type(a), type(b), type(c))

print(123)
print(0o123)
print(0x123)
print(bin(123))
print(0b101101)

a = 0.002
b = 2e-4

print(b)

try:
	a = 21
	b = "poloska"
	print(a/b)
except ValueError:
	print(ValueError)
except TypeError:
	print(TypeError)