"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).

Output: The most frequent letter in lower case as a string.

Example:

checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!
"""
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

	for j in list_sort_by_key:
		if first_pice == j[1]:
			conjuction +=1

	# print list_sort_by_key
	
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
print checkio(u"Hello World!")
print checkio(u"How do you do?")
print checkio(u"One")
print checkio(u"Oops!")
print checkio(u"AAaooo!!!!")
print checkio(u"abe")
print("Start the long test")
print checkio(u"a" * 9000 + u"b" * 1000)
print("The local tests are done.")