import string
diction_l = string.ascii_lowercase
def checkio(string):
	count_l = {}
	z = string.encode('ascii','replace')
	new_string = str.lower(z)
	for y in diction_l:
		count_l[y]= 0
	for x in new_string:
		if x in diction_l:
			count_l[x] +=1
	print sorted(count_l.values())

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
