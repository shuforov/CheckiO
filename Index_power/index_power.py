#Index power

def index_power(list_n, n_num):
	if ((len(list_n) > 0) and (len(list_n) <= 10)) and ((n_num >= 0) and (n_num <= 100)):
		if len(list_n) > n_num:
			return list_n[n_num] ** n_num
		else :
			return -1

print index_power([1, 2, 3, 4], 2)
print index_power([1, 3, 10, 100], 3)
print index_power([0, 1], 0)
print index_power([1, 2], 3)