

#lista <-> tuple
# -egyszer lehet megszabni
# -nem változtatható
# -lehet azonos elem benne
# -van sorrend
# -több érték egyszerre külön típus
# - [] helyett ()

# 1) feladat

"""def main():
	list = []
	for i in range(5):
		c = False
		while c == False :
			name = str ( input ( "Név: " ) )
			score = int ( input ( "Pontszám: " ) )
			if score >= 0 and score <= 100:
				temp = (name, score)
				list.append(temp)
				c = True
			else:
				print("Helytelen adatok! 0 <= Pontszám <= 100")
	return list

tupli = tuple(main())

for i in range(5):
	if tupli[i][1] < 40:
		print("egy.")
	elif tupli[i][1] < 55:
		print("káttű")
	elif tupli [i][1] < 70:
		print("három")
	elif tupli[i][1] < 85:
		print("nyég")
	else:
		print("ötös")

min = 0
max = 0

for i in range(5):
	if tupli[i][1] > tupli[max][1]:
		max = i
	elif tupli[i][1] < tupli[min][1]:
		min = i

print(f"Minimum: {tupli[min]}, Maximum: {tupli[max]}")

def sum():
	o = 0
	for i in tupli:
		o+i[1]

print(f"Összeg: {sum()}")
print(f"Átlag: {sum()/len(tupli)}")"""

# numero dos

data = input("Adj meg egy adatot --> ")
data1 = input ( "Adj meg egy adatot --> " )
data2 = input ( "Adj meg egy adatot --> " )

teknos = (data, data1, data2)

data3 = input ( "Adj meg egy adatot --> " )
data4 = input ( "Adj meg egy adatot --> " )
data5 = input ( "Adj meg egy adatot --> " )

kenguru = (data3 , data4 , data5)

if list(kenguru).sort() == list(teknos).sort():
	print("egyenlőség és világbéke")
else:
	print("A teknős felsőbbrendű.")



"""if __name__ == "__main__":
	print(tupli)"""