#  File: Benford.py

#  Description: This program reads a text file containing the population of each city, in each 
#  state, and reports the frequency distribution of the the first digit of the 
#  population numbers

#  Date Created: 27 November 2017

#  Date Last Modified: 29 November 2017

def leadingDigit (num):

	
	# This function can take as an argument either 
  	# a float or integer value and will compute that 
  	# value's leading digit using recursion


	if (num < 10):
		return (int (num))
	else:
		return leadingDigit (num // 10)


def main():

   # create and initialize dictionary 
	popFrequency = {x: 0 for x in range (1, 10)}

	print ("")
   # open file for reading
	with open ("Census_2009.txt", "r") as inFile:
	
	   # keeps track of total data points for finding mean
		dataPoints = 0	

	   # read header and ignore		
		header = inFile.readline()

	   # read lines of the file and find leading digit
		for line in inFile:
			popData = line.rstrip().split()
			popNum = int (popData [-1])
			leadDigit = leadingDigit(popNum)
			dataPoints += 1

		   # match leadDigit to key in dictionary and increment its value
			for key in popFrequency:
				if (key == leadDigit):
					popFrequency[key] += 1

   # print header
	print ("{:^10} {:>6} {:>11}".format ("Digit", "Count", "%")) 
	
   # format and print computed data
	for key in popFrequency:
	   # compute the mean and set result to correct decimal places
		mean = (int ((popFrequency [key] / dataPoints) * 10000)) / 100	
		print (("{:^10}{:^10}{:>10.1f}%").format(key, popFrequency [key], mean))
	print("") 

main ()
