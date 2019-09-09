

#  Q. Write a function that takes as input two strings and returns True
#  if the two string are anagrams and False otherwise. The strings may
#  have spaces and punctuation marks and upper and lower characters. You
#  are only concerned that they have the same letters (case insensitive)

def isAnagram (string1, string2):

	string1 = string1.lower()
	string2 = string2.lower()
	count = 0
	if (count == 0) and (len(string1) == len(string2)):
		count += 1
		if (len (string1) == 0):
			return True
		elif (string1[0].isalpha()):
			if (string2.find(string1[0]) != -1):
				string2[0:string2.find(string1[0])] + string2[string2.find(string1[0]) + 1 : len(string2) + 1]
				return isAnagram (string1[1:], string2)
			else:
				return False
		else:
			return isAnagram (string1[1:], string2)


def main ():

	string1 = input ("Enter the first string: ")
	string2 = input ("Enter the second string: ")
	if (isAnagram (string1, string2) == True):
		print ("True")
	else: 
		print ("False")

main ()
