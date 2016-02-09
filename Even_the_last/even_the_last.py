#Even_the_last

def checkio(list_n):
	if len(list_n) > 0:
		z = list_n[0::2]
		v = 0
		for x in z:
			v += x
		return v * list_n[-1]
	elif len(list_n) == 0:
		return 0

print checkio([0, 1, 2, 3, 4, 5])
print checkio([1, 3, 5])
print checkio([6])
print checkio([])