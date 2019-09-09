#  Description: Given a text file with deminsions of boxes, return a list of 
#  the longest subset(s) which may be nested inside of each other

# read in text file and put deminsions in a list in descending order
def read_txt ():

	dims = []

	with open ("boxes.txt", "r") as in_file:
		n = int(in_file.readline ())
		for line in in_file:
			line = line.rstrip().split()
			line = [int(i) for i in line]
			line.sort()
			dims.append(line)
	dims.sort()

	return n, dims

# Compares two boxes and returns True if box1 is strictly less than box2
def compare_boxes (box1, box2):

	return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

# Returns all subsets of a 2-D list
def subsets (list_a, list_b, n, start):

	subs = []

	if (start == n):
		subs.append(list_b)
	else:
		list_c = list_b[:]
		list_b.append (list_a[start])
		return subsets (list_a, list_b, n, start + 1) + subsets (list_a, list_c, n, start + 1)

	return subs

# Returns the largest subset which contains boxes that may be nested 
def big_subset (sub_list):
	
	largest_sub = []
	fitting_subs = []
	len_sub = 0


	# Confirm subsets in largest_subset contain nested boxes
	for sub in range (len (sub_list)):
		if len (sub_list[sub]) > 1:
			for box in range (1, len (sub_list[sub])):
				if compare_boxes (sub_list[sub][box - 1], sub_list[sub][box]):
					if box + 1 == len(sub_list[sub]):
						fitting_subs.append(sub_list[sub])
				else:
					break
		else: 
			pass

	# Find largest subset length
	for sub in range (len(fitting_subs)):
		if len(fitting_subs[sub]) >= len_sub:
			len_sub = len(fitting_subs[sub])
		else:
			continue

	# Append subsets with length equal to the largest subset length
	for sub in range (len(fitting_subs)):
		if (len(fitting_subs[sub]) == len_sub):
			largest_sub.append(fitting_subs[sub])
		else: 
			continue

	return largest_sub
	
def main():

	largest_sub = []
	sub_list = []

	n, dims = read_txt()

	sub_list = subsets(dims, sub_list, n, 0)

	largest_sub = big_subset(sub_list)

	if len (largest_sub[0]) > 1:
		print ("Largest Subset of Nesting Boxes")
		for sub in range (len(largest_sub)):
			for box in range (len(largest_sub[sub])):
				print (tuple(largest_sub[sub][box]))
			print ()
	else:
		print ("No Nesting Boxes")

main()
