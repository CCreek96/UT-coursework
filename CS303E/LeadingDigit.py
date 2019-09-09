def leadingDigit (num):
	
	''' This function can take as an argument either 
  	    a float or integer value and will compute that 
  	    value's leading digit using recursion						
	'''

	if (num < 10):
		return (int (num))
	elif (len (num) % 2):
		return leadingDigit (num // 10)


def main ():

	num = eval (input ("Enter number to get first digit: "))
	print (leadingDigit (num))

main ()