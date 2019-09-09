'''
  Q. Given a dictionary with a unique set of keys and values,
  like countries and their capitals, create a dictionary
  where the value is the key and the key is the value, i.e.
  a dictionary of capitals and their countries.'''

def keyValSwap (orig_dict):
	new_dict = {}
	for key in orig_dict:
		new_dict[orig_dict[key]] = key
	return new_dict

def main ():

	orig_dict = {"U.S.A" : "D.C.", "France" : "Paris", "England" : "London"}
	new_dict = keyValSwap (orig_dict)
	for key in new_dict:
		print (key, " ", new_dict[key])

main ()