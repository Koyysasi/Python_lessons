
def leggyakoribb_szoveg_a_fajlban(fname):

	dataPairs = dict()
	maxKey = ""

	with open(fname, "r") as data:
		f = data.readlines()
		for e in f:

			print(e)

			for i in e:
				trueI = i.strip()

				if i.lower() == i.upper():
					continue

				if trueI in dataPairs.keys():
					dataPairs[trueI] += 1
					if dataPairs[trueI] >= max(dataPairs.values()):
						maxKey = trueI

				else:
					dataPairs[trueI] = 1
					if dataPairs[trueI] >= max(dataPairs.values()):
						maxKey = trueI

	print(dataPairs)
	return (max(dataPairs.values()), maxKey)

def leggyakoribb_alternativa(fname):
	szotar = dict()
	with open(fname, "r") as data:
		f = data.readlines()

	karakterek = list()

	for sor in f:
		k = list(sor)
		karakterek += k

	for k in karakterek:
		if str(k).lower() == str(k).upper():
			karakterek.remove(k)

	print(karakterek)



print(leggyakoribb_szoveg_a_fajlban("harcsafile.txt"))
