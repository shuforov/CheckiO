
def checkio(list_n):
	sorting = sorted(list_n)
	len_l = len(sorting)
	print sorting
	if (len_l % 2) == 1:
		return sorting[(len_l / 2)]
	elif (len_l % 2) == 0:
		return float(sorting[((len_l/2)-1)] + sorting[(len_l / 2)]) / 2

print checkio([1, 2, 3, 4, 5])
print checkio([3, 1, 2, 5, 3])
print checkio([1, 300, 2, 200, 1])
print checkio([3,6,20,99,10,15])