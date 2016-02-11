import string
diction_l = string.ascii_lowercase # creating of 
def getKey(item):
	return item[1]

def in_tapl(tap_o):
	first_tapl = tap_o[1]
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
	most_wanted_letter = list_sort_by_key[0]
	print
	print length_of_tapl
	print
	print list_sort_by_key
	print list_sort_by_letters


	return most_wanted_letter[0]



#These "asserts" using only for self-checking and not necessary for auto-testing
print checkio(u"fsssbbbd")

