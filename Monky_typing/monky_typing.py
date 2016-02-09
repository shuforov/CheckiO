#Monky_typing

def count_words(str_s,tuple_t):
	q = 0
	for x in tuple_t:
		z = str_s.encode('ascii','replace')
		z = str.lower(z)
		if x in z:
			q += 1
	return q

print count_words("How aresjfhdskfhskd you? you?", {"how", "are", "you", "hello"})
print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
print count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"})
