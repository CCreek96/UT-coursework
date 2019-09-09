# Exam review question

#Q. Create a function that accepts a string as an input 
#parameter and then prints out the frequency of all the
#characters other than white space characters. Use a
#dictionary and parse the input string character by
#character. The character will be the key and the
#frequency of its occurence the value. Print all the
#key-value pairs at the end.

def charFrequency (st):

	char_dict = {}

	for char in st:
		if (char.isalpha()):
			if (char in char_dict):
				char_dict[char] += 1
			else:
				char_dict[char] = 1
		else:
			continue
	return char_dict


def main ():

	string = input ("Enter a string: ")
	char_dict = charFrequency (string)
	for key in char_dict:
		print (key, " ", str(char_dict[key]))

main ()
