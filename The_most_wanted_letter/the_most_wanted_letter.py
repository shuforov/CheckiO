import string
diction_l = string.ascii_lowercase
def checkio(string):
	count_l = {}
	new_count = []
	z = string.encode('ascii','replace')
	new_string = str.lower(z)
	for y in diction_l:
		count_l[y]= 0
	for x in new_string:
		if x in diction_l:
			count_l[x] +=1
	for h in count_l:
		if count_l[h] > 0:
			new_count.append((h,count_l[h]))
	print new_count
	for aa in new_count:
		print aa
		if aa[1] > 2:
			print aa[0]
		
	# print new_count
	# t = sorted(count_l.items())
	# print t.sort()
	# j = sorted(new_count.values())
	# print j[-1:]

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
