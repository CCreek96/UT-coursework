from string import punctuation
def parseString (st):
	
	if (len (st) == 0):
		return st
	elif (st [-1] == "'"):
		return ("") + parseString (st [1:])
	elif (st [0] == "'" and st[1] in punctuation):
		return ("") + parseString (st [2:])
	elif (st [:2] == "'s"):
		return ("") + parseString (st [2:])
	elif (not (st [0].isalpha() or st[0].isspace())) and (st[0] != "'"):
		return (" ") + parseString (st [1:])
	elif (st [0] in punctuation and st [0] != "'"):
		return (" ") + parseString (st [1:])
	else:
		return st[0] + parseString (st [1:])


def main ():
	print ("")
	sentence = input ("Enter a sentence with punction marks: ")
	print ("")
	new_st = parseString (sentence)

	print ("Your sentence without punctuation marks is:", "\n")
	
	print (new_st)
	print ("")

main ()