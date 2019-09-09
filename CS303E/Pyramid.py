# Excercise 5.19

def main ():

  lines = int (input ("\nEnter the number of lines: "))

  for i in range (1, lines + 1):
  	for j in range (i, 1, -1):
  	  print (j, end = " ")
  	for k in range (1, i + 1):
  	  print (k, end = " ")
  	print ()

main ()