import string
diction_l = string.ascii_lowercase
def getKey(item):
	return item[1]

def checkio(string):
	count_l = {}
	converted_list_from_count_l = []
	z = string.encode('ascii','replace')
	new_string = str.lower(z)
	for le in new_string:
		if le in diction_l:
			count_l[le] = 0
	for le_update in new_string:
		if le_update in diction_l:
			count_l[le_update] += 1
	for element in count_l:
		converted_list_from_count_l.append((element, count_l[element]))
	list_sort_by_key = sorted(converted_list_from_count_l, key=getKey, reverse=True)
	list_sort_by_le = sorted(converted_list_from_count_l)
	disp_le = list_sort_by_key[0]
	print list_sort_by_key
	print list_sort_by_le
	return disp_le[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
print checkio(u"fsbd")

