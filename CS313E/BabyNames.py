#  File: BabyNames.py 

#  Description: Simulate a database for baby name popularity for decades 1900-2000, allowing 
#  a user to choose between six different options that will output different data.

#  Date Created: 20 March 2018

#  Date Last Modified: 24 March 2018

import urllib.request
from collections import OrderedDict

# Create global word dictionary from imported text file 
baby_names = {}
def make_dict ():

	try:
		url = 'http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt'

		with urllib.request.urlopen(url) as response:
			data = response.read().decode('utf-8')
			text = data.split('\n')
			for idx in range(len(text)):
				text[idx] = text[idx].split()
				line = text[idx]
				if (len(line) > 0):
					name = line[0]
					data = line[1:12]
					for item in range (len(data)):
						data[item] = int(data[item])
						if data[item] == 0:
							data[item] = 1001
					baby_names[name] = data
				else:
					continue
			return
	except HTTPError as ex:
		err_msg = ex.read()

# Menu choice 1; return True and highest decade if name in 
# dictionary, and false otherwise
def name_in_dict (name):
	high = 1002
	decade = 0        # list index representing decade
	if name in baby_names:
		values = baby_names[name]
		for idx in range (len (values)):
			if values[idx] < high: 
				high = values[idx] 
				decade = idx
			else:
				continue
		print ('\nThe matches with their highest ranking decade are:')
		if decade in range (0, 10):
			print (name, '19{}0'.format(decade))
		elif decade == 10:
			print (name, '2000')
		return True
	else:
		print ()
		print (name, 'does not appear in any decade.')
		return False

# Menu choice 2; returns all the rankings for a given name
def name_ranks (name):
	if name in baby_names:
		for key in baby_names:
			if (key == name):
				values = baby_names[key]
				valP1 = values[0:6]
				valP2 = values[6:]
				print (name + ':' + ' {} {} {} {} {} {} {} {} {} {} {}'.format(*values))
				print ('1900: {}\n1910: {}\n1920: {}\n1930: {}\n1940: {}\n1950: {}'.format(*values[0:6]))
				print('1960: {}\n1970: {}\n1980: {}\n1990: {}\n2000: {}\n'.format(*values[6:]))
	else:
		print (name, 'does not appear in any decade')


# Menu choice 3; displays all the names that have a rank in a 
# given decade in order of rank 
def names_rank_spec_decade(decade): 

   # Convert input decade to iterable value
	if decade == '2000':
		decade = 10
	else:
		decade.split()
		decade = int(decade[2])
   # pass baby_name keys with a rank in the specified decade
	temp_dict = {}
	for key in baby_names:
		values = baby_names[key]
		if values[decade] == 1001:
			pass
		else:
			temp_dict[key] = values[decade]
   # order dictionary based on values
	ordered_temp_dict = OrderedDict(sorted(temp_dict.items(), key = lambda x: x[1]))
	print ('The names are in order of rank:')
	for key, val in ordered_temp_dict.items():
		print (key +  ': ' + str(val))

# Menu choice 4; returns a list of names that have a rank in 
# all the decades in sorted order by name
def names_rank_all_decades():
   # pass baby_name keys with a rank in all decade
	temp_dict = {}
	for key in baby_names:
		values = baby_names[key]
		if 1001 in values:
			pass
		else:
			temp_dict[key] = values

	print('{} names appear in every decade. The names are:'.format(len(temp_dict)))
	for key in temp_dict:
		print (key)

# Menu choice 5; display all names that are getting more popular in every decade
def increasing_popularity ():

	temp_dict = {}
	compare = 1002
	for key in baby_names:
		values = baby_names[key]
		compare = 1002
		if 1001 not in values:
			for item in range(len(values)):
				if item == len(values) - 1:
					if compare >= values[item]:
						temp_dict[key] = values
				else:
					if compare >= values[item]:
						compare = values[item]
						continue
					else:
						break
		else:
			pass

	print('{} names are more popular in every decade.'.format(len(temp_dict)))
	for key in temp_dict:
		print (key)

# Menu choice 6; display all names that are getting less popular in every decade
def decreasing_popularity ():

	temp_dict = {}
	compare = 0
	for key in baby_names:
		values = baby_names[key]
		compare = 0
		if 1001 not in values:
			for item in range(len(values)):
				if item == len(values) - 1:
					if compare <= values[item]:
						temp_dict[key] = values
				else:
					if compare <= values[item]:
						compare = values[item]
						continue
					else:
						break
		else:
			pass

	print('{} names are less popular in every decade.'.format(len(temp_dict)))
	for key in temp_dict:
		print (key)

def main():

	menu = ('\nOptions:\n'
	'Enter 1 to search for names.\n'
	'Enter 2 to display data for one name.\n'
	'Enter 3 to display all names that appear in only one decade.\n'
	'Enter 4 to display all names that appear in all decades.\n'
	'Enter 5 to display all names that are more popular in every decade.\n'
	'Enter 6 to display all names that are less popular in every decade.\n'
	'Enter 7 to quit.\n')

	make_dict()
	print (baby_names)

	print (menu)
	menu_choice = int (input('Enter choice: '))

	while True:
		if (menu_choice == 1):
			name = input('Enter a name: ')
			name_in_dict(name)
		elif (menu_choice == 2):
			name = input('Enter a name: ')
			print()
			name_ranks(name)
		elif (menu_choice == 3):
			decade = input('Enter a decade: ')
			print()
			while (decade not in ['1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000']):
				decade = input('Enter a decade: ')
				print()
			names_rank_spec_decade(decade)
		elif (menu_choice == 4):
			names_rank_all_decades()
		elif (menu_choice == 5):
			increasing_popularity()
		elif (menu_choice == 6):
			decreasing_popularity()
		else:
			break

		print (menu)
		menu_choice = int(input('Enter choice: '))

	print ('\nGoodbye.\n')
		

main()
