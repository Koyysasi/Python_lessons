'''
Feladat: Leggyakoribb szám a szövegfájlban.
Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
A függvény bemenő paramétere a fájl neve.
'''

def leggyakoribb_szam_a_fajlban(szia):
	szotar = dict()
	f = open("szamok1.txt", "r")
	szia = f.readlines()
	f.close()

	for sor in szia:
		if sor in szotar.keys():
			szotar[sor] += 1
		else:
			szotar[sor] = 1

	maxszam = max(szotar.values())


