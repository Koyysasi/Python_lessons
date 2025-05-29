1101001010

print()

def bintodec(num, graph = False):
	final = 0
	rev = num[::-1]
	for e in range(len(rev)):
		final+=int(rev[e])*pow(2, e)
	return final

print(bintodec("011", True))

# Bitwise cuccok

a = 0b010101
b = 0b110011

# AND
print(a & b)

# OR
print(a | b)

# XOR
print(a ^ b)

# NOT
print(~a, ~b)

# shift
print(a << b)
print(a >> b)

def is_bit_set(num, index):
	return str(bin(num))[index+2] == "1"

print(is_bit_set(2, 0))
