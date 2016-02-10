
def checkio(list_n):
	g = []
	for x in list_n:
		z = list_n.count(x)
		if z > 1:
			g.append(x)
	return g
print checkio([1,2,3,1,3])
print checkio([1, 2, 3, 4, 5])
print checkio([5, 5, 5, 5, 5])
print checkio([10, 9, 10, 10, 9, 8])