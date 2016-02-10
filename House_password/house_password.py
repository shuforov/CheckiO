import string
list_l = string.ascii_lowercase
list_u = string.ascii_uppercase
num = string.digits

def checkio(text_s):
	low_check = ""
	upper_check = ""
	numbers_check = ""

	if len(text_s) >= 10:
		for letter_l in list_l:
			if letter_l in text_s:
				low_check = True
		for letter_u in list_u:
			if letter_u in text_s:
				upper_check = True
		for number_n in num:
			if number_n in text_s:
				numbers_check = True

	if (low_check and upper_check and numbers_check) == True:
		return True
	else:
		return False

print checkio('A1213pokl')
print checkio('bAse730onE')
print checkio('asasasasasasasaas')
print checkio('QWERTYqwerty')
print checkio('123456123456')
print checkio('QwErTy911poqqqq')