#  File: Books.py

#  Description: This program prompts a user for the name of two books 
#  given as text files as well as the authors' names. It then compares 
#  for each respective author the number of distinct words, total words, 
#  the ratio of distinct to total words, the number of distinct words 
#  used by one of the authors but not the other and vice versa, and that 
#  number as a ratio to the authors' total words.

#  Date Created: 29 November 2017

#  Date Last Modified: 05 December 2017

from string import punctuation
from collections import OrderedDict

# Create global word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():

	with open ("words.txt") as in_file:
		for line in in_file:
			words = line.rstrip()
			word_dict[words] = 1

# Remove punctuation marks from a string using recursive function
def parseString (st):

	if (len (st) == 0):
		return st
	elif (not (st [0].isalpha() or st[0].isspace())):
		if (not (st [0] in punctuation)):
			return ("") + parseString (st [1:])
		elif (st [0] == "'"):
			if (len (st) == 1):
				return ("") + parseString (st [1:])
			elif (st [1].isspace ()):
				return (" ") + parseString (st [2:])
			elif (st [1] == "s"):
				return ("") + parseString (st [2:])
			else: 
				return st[0] + parseString (st [1:])
		else: 
			return (" ") + parseString (st [1:])
	else:
		return st[0] + parseString (st [1:])

# Returns a dictionary of words and their frequencies
def getWordFreq (file):

	capital_words = []
	word_freq_dict = {}
	with open (file) as in_file:
		for line in in_file:
			line = line.rstrip()
		   # Remove punctuations from the string
			line_processed = parseString (line)
			words = line_processed.split()

		   # Capital words added to list and all others added to frequency dictionary
			for word in words:
				if (word.islower()):
					if (word in word_freq_dict):
						word_freq_dict [word] += 1
					else:
						word_freq_dict [word] = 1
				else:
					capital_words.append(word) 

   # Check if capital words in list are in frequency or global dictionary
	for word in capital_words:
		word_lower = word.lower()

	   # If it is in frequency dictionary, increment it's value
		if (word_lower in word_freq_dict):
			word_freq_dict [word_lower] += 1

	   # If not in frequency dictionary, but is in global dictionary; 
	   # add the word to frequency dictionary 
		elif (word_lower in word_dict):
			word_freq_dict [word_lower] = 1
		else:
			continue

	return word_freq_dict

# Compares the distinct words in two dictionaries
def wordComparison (author1, word_freq1, author2, word_freq2):
   
   # For each author, compute number of distinct words, 
   # total words, and their ratio; then print the result

   # Author 1
	key_list1 = word_freq1.keys()
	num_unique_words1 = len (key_list1)
	total_words1 = sum (word_freq1.values())
	word_ratio1 = (num_unique_words1 / total_words1) * 100
	print (author1)
	print ('Total distinct words = ', num_unique_words1)
	print ('Total words (including duplicates) = ', total_words1)
	print ("Ratio (%", "of total distinct words to total words) = ", round (word_ratio1, 10), "\n")

   # Author 2
	key_list2 = word_freq2.keys()
	num_unique_words2 = len (key_list2)
	total_words2 = sum (word_freq2.values())
	word_ratio2 = (num_unique_words2 / total_words2) * 100
	print (author2)
	print ('Total distinct words = ', num_unique_words2)
	print ('Total words (including duplicates) = ', total_words2)
	print ("Ratio (%", "of total distinct words to total words) = ", round (word_ratio2, 10), "\n")


   # Find set differences and relative frequency
	D = set (key_list1)
	H = set (key_list2)
	diff_author1 = D - H
	diff_author2 = H - D
	rel_freq_author1 = 0
	rel_freq_author2 = 0

   # Add the value of keys in both set differences
	for key1 in diff_author1:
		rel_freq_author1 += word_freq1[key1]
	for key2 in diff_author2:
		rel_freq_author2 += word_freq2[key2]

   # Compute the ratio of relative frequencies to total words
	set_diff_D = (rel_freq_author1 / total_words1) * 100
	set_diff_H = (rel_freq_author2 / total_words2) * 100

   # Print results
	print ("{} used {} words that {} did not use.".format (author1, len (diff_author1), author2))
	print ("Relative frequency of words used by {} not in common with {} = {}".format (author1, author2, round (set_diff_D, 10)), "\n")
	print ("{} used {} words that {} did not use.".format (author2, len (diff_author2), author1))
	print ("Relative frequency of words used by {} not in common with {} = {}".format (author2, author1, round (set_diff_H, 10)), "\n")

   # Print dictionaries to check for errors
	diff_author_dict1 = {}
	diff_author_dict2 = {}
	for item1 in diff_author1:
		diff_author_dict1 [item1] = word_freq1 [item1]
	for item2 in diff_author2:
		diff_author_dict2 [item2] = word_freq2 [item2]

   # Author 1
	with open ("Author1.out.txt", "w") as AuthorOut1:
		word_freq1 = OrderedDict (sorted (word_freq1.items()))
		diff_author_dict1 = OrderedDict (sorted (diff_author_dict1.items()))
		count1 = 0
		while (count1 < 2):
			if (count1 < 1):
				AuthorOut1.write ("All the distinct words that " + author1 + " used: \n\n")
				for key in word_freq1:
					AuthorOut1.write (str(word_freq1 [key]) + "	" + key + "\n")
				count1 += 1
			else:
				AuthorOut1.write ("\n\nAll the words that " + author1 + " used, but " + author2 + " did not use: \n\n")
				for key in diff_author_dict1:
					AuthorOut1.write (str(diff_author_dict1 [key]) + "	" + key + "\n")
				count1 += 1
   # Author 2
	with open ("Author2.out.txt", "w") as AuthorOut2:
		word_freq2 = OrderedDict (sorted (word_freq2.items()))
		diff_author_dict2 = OrderedDict (sorted (diff_author_dict1.items()))
		count2 = 0
		while (count2 < 2):
			if (count2 < 1):
				AuthorOut2.write ("All the distinct words that " + author2 + " used: \n\n")
				for key in word_freq2:
					AuthorOut2.write (str(word_freq2 [key]) + "	" + key + "\n")
				count2 +=1
			else:
				AuthorOut2.write ("\n\nAll the words that " + author2 + " used, but " + author1 + " did not use: \n\n")		
				for key in diff_author_dict2:
					AuthorOut2.write (str(diff_author_dict2 [key]) + "	" + key + "\n")
				count2 += 1

def main ():

   # Create word dictionary from comprehensive word list
	create_word_dict()

	print ("") # Spacer for readibility

   # Enter names of the two books in electronic form
	book1 = input ("Enter name of first book: ")
	book2 = input ("Enter name of second book: ")

	print("") # Spacer for readibility

   # Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")

	print("") # Spacer for readability
  
   # Get the frequency of words used by the two authors
	word_freq1 = getWordFreq (book1)
	word_freq2 = getWordFreq (book2)

   # Compare the relative frequency of uncommon words used by the two authors
	wordComparison (author1, word_freq1, author2, word_freq2)

main ()
