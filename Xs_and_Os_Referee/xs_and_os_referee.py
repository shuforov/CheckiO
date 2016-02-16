# -*- coding: utf-8 -*-

def checkio(list_x):
	X_list = []
	O_list = []
	D_list = []
	def make_a_list(list_n):
		for list_1 in list_n:
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

	make_a_list(list_x)			

	#print "X got this -> ",X_list
	#print "O got this -> ",O_list
	#print "D got this -> ",D_list

	def check_all(list_check_x,list_check_o,list_check_d):
		#check X list_win?
		def check_x(list_check_x):
				#check in thw horizontal
			if [0,1,2] in list_check_x:
				return "X"
				#check in the vertical	
			zero_count = 0
			one_count = 0
			two_count = 0
			for num_x in list_check_x:
				if 0 in num_x:
					zero_count += 1
			if zero_count == 3:
				return "X"
			for num_x in list_check_x:
				if 1 in num_x:
					one_count += 1
			if one_count == 3:
				return "X"
			for num_x in list_check_x:
				if 2 in num_x:
					two_count += 1
			if two_count == 3:
				return "X"
				#check in the diagonal
			if (0 in list_check_x[0])and (1 in list_check_x[1]) and (2 in list_check_x[2]):
				return "X"
			if (2 in list_check_x[0]) and (1 in list_check_x[1]) and (0 in list_check_x[2]):
				return "X"
		X_res = check_x(X_list)
		#check O list_win?
		def check_o(list_o):
			#check in thw horizontal
			if [0,1,2] in list_check_o:
				return "O"
				#check in the vertical	
			zero_count_o = 0
			one_count_o = 0
			two_count_o = 0
			for num_o in list_check_o:
				if 0 in num_o:
					zero_count_o += 1
			if zero_count_o == 3:
				return "O"
			for num_o in list_check_o:
				if 1 in num_o:
					one_count_o += 1
			if one_count_o == 3:
				return "O"
			for num_o in list_check_o:
				if 2 in num_o:
					two_count_o += 1
			if two_count_o == 3:
				return "O"
				#check in the diagonal
			if (0 in list_check_o[0])and (1 in list_check_o[1]) and (2 in list_check_o[2]):
				return "O"
			if (2 in list_check_o[0]) and (1 in list_check_o[1]) and (0 in list_check_o[2]):
				return "O"
		O_res = check_o(O_list)
			#check D_
		def check_d(list_check_d):
			count_d = 0
			for ch_l in list_check_d:	
				if len(ch_l) == 0:
					count_d +=1
			if count_d == 3:
				return "D"
		D_res = check_d(D_list)
		if X_res == "X":
			return "X"
		elif O_res == "O":
			return "O"
		elif D_res == "D":
			return "D"
		else:
			return "D"
	return check_all(X_list,O_list,D_list)

print checkio([
    "OXO",
    "XOX",
    ".XO"])
