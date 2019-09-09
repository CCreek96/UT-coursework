
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

	   # read lines of the file and find leading number
		for line in inFile:
			popData = line.rstrip().split()
			popNum = popData [-1]
			leadDigit = int (popNum[0])
			dataPoints += 1

		   # match leadDigit to key in dictionary and increment its value
			for key in popFrequency:
				if (key == leadDigit):
					popFrequency[key] += 1

   # header for output
	print ("{:^10} {:>6} {:>11}".format ("Digit", "Count", "%")) 
	
   # format and print computed data
	for key in popFrequency:
	   # compute the mean and set result to correct decimal places
		mean = (popFrequency [key] / dataPoints)
		europeanSwallow = int (mean * 1000)				
		africanSwallow = europeanSwallow / 10			
		print (("{:^10}{:^10}{:>10.1f}%").format(key, popFrequency [key], africanSwallow))
	print("") 

main ()