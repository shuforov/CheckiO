import string
diction_l = string.ascii_lowercase # creating of 
def getKey(item):
	return item[1]

def in_tapl(tap_o):
	first_tapl = tap_o[0]
	return first_tapl[1]

def checkio(string):
	count_letters = {}
	converted_list_from_count_letters = []
	decode_from_uni_to_str = string.encode('ascii','replace')
	new_string = str.lower(decode_from_uni_to_str)
	for letter in new_string:
		if letter in diction_l:
			count_letters[letter] = 0
	for letter_update in new_string:
		if letter_update in diction_l:
			count_letters[letter_update] += 1
	for element in count_letters:
		converted_list_from_count_letters.append((element, count_letters[element]))
	#check the letter
	conjuction = 0
	length_of_tapl = len(converted_list_from_count_letters)
	list_sort_by_key = sorted(converted_list_from_count_letters, key=getKey, reverse=True)
	list_sort_by_letters = sorted(converted_list_from_count_letters)
	maximum = max(list_sort_by_key)
	max_num = maximum[1]
	first_pice = in_tapl(list_sort_by_key)
	most_wanted_letter_one = list_sort_by_key[0]
	most_wanted_letter_two = list_sort_by_letters[0]

	for j in list_sort_by_key:
		if first_pice == j[1]:
			conjuction +=1
			print j
	print first_pice
	print 
	print max_num
	print 
	print conjuction
	# print list_sort_by_key
	print list_sort_by_letters
	
	temp_list = []
	
	if conjuction == 1:
		for t_l in list_sort_by_key:
			if first_pice == t_l[1]:
				temp_list.append(t_l)
	elif conjuction >= 2:
		for t_l in list_sort_by_key:
			if first_pice == t_l[1]:
				temp_list.append(t_l)

	temp_list_2 = sorted(temp_list)
	temp_list_3 = temp_list_2[0]

	return temp_list_3[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
print checkio(u"Lorem ipsum dolor sit amet")

