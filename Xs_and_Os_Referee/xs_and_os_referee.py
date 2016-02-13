# -*- coding: utf-8 -*-

def checkio(list_x):
	X_list = []
	O_list = []
	D_list = []

	list_of_vin = [[[0,1,2]],[[0],[0],[0]],[[1],[1],[1]],[[2],[2],[2]],[[0],[1],[2]],[[2],[1],[0]]]

	for list_1 in list_x:
		element_x = []
		element_o = []
		element_dot = []
		count = 0
		for element in list_1:
			if element == "X":
				element_x.append(count)
			elif element == "O":
				element_o.append(count)
			elif element == ".":
				element_dot.append(count)
			count +=1
		X_list.append(element_x)
		O_list.append(element_o)
		D_list.append(element_dot)

	count_1 = 0
	for ch_l in D_list:	
		if len(ch_l) == 0:
			count_1 +=1
	
	if count_1 == 3:
		return "D"
	
	X_zero_count = 0
	X_one_count = 0
	X_two_count = 0

	for l in X_list:
		if len(l) == 1:
			if l[0] == 0:
				X_zero_count += 1
			elif l[0] == 1:
				X_one_count += 1
			elif l[0] == 2:
				X_two_count += 1	
		elif len(l) >= 2:
			if l[1] == 1:
				X_one_count +=1

	if X_zero_count == 3:
		return "X"
	elif X_one_count == 3:
		return "X"
	elif X_two_count == 3:
		return "X"

	print X_list
	print O_list
	print D_list

print checkio([
    "OOX",
    "OXX",
    "X.X"])