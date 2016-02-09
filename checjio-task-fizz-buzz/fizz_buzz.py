#fizz buzz

def fizz_buzz(num_f):
	if (num_f > 0) and (num_f <= 1000):
		if ((num_f % 3) == 0) and ((num_f % 5) == 0):
			return "Fizz Buzz"
		elif (num_f % 3) == 0:
			return "Fizz"
		elif (num_f % 5) == 0:
			return "Buzz"
		else :
			return num_f
	else:
		return "Number incorrect, it mast be in range from 0 to 1000"
	

print fizz_buzz(15)
print fizz_buzz(6)
print fizz_buzz(5)
print fizz_buzz(7)