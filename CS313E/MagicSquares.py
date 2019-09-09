
#  File: MagicSquare.py

#  Description: This program creates a magic square for odd numbers greater than 
   or equal to three in a 2-D list and confirms that it is indeed a magic square

# Populate a 2-D list with numbers from 1 to n^2
def make_square (dim):

 # Create and initailize a 2-D list and the starting position
  magic_square = [[None for col in range (dim)] for row in range (dim)]
  col = dim // 2 
  row = dim - 1 
  num = 1

  while (num <= (dim ** 2)):
     # Check if outside row and column 
      if col == dim and row == dim: 
          row = dim - 2
          col = dim - 1
     # Check if outside of right column
      elif (row == dim):
        row = 0
     # Check if outside of bottom row
      elif (col == dim):
        col = 0
     # Confirm index has not been editted and insert value           
      if (magic_square[row][col] != None):
          row -= 2
          col -= 1
          continue
      else:
          magic_square[row][col] = num
          num += 1   
     # Move to next position
      row += 1
      col += 1 
  return magic_square
    
# Print magic square in a right justified format 
def print_square (magic_square):

  print ("Here is a {} x {} magic square:".format(len(magic_square),len(magic_square)), "\n")
  for row in range (len(magic_square)):
    for elem in range (len(magic_square)):
      print (("{:>3}").format(magic_square[row][elem]), end = " ")
    print ()

# Check that the 2-D list generated is indeed a magic square
def check_square (magic_square):

 # Calculate canon sum
  canon_sum = len(magic_square) * (len(magic_square) ** 2 + 1) / 2

 # Sum each row 
  for i in range (len(magic_square)):
    sum_row = 0
    for j in range (len(magic_square[i])):
      sum_row += magic_square[i][j]
 # Sum each column
  for i in range (len (magic_square[0])):
    sum_column = 0
    for j in range (len(magic_square)):
      sum_column += magic_square[j][i]

 # Sum the diagonal going left to right
  sum_lr = 0
  for i in range (len(magic_square)):
    sum_lr += magic_square[i][i]
 # Sum the diagonal going right to left
  sum_rl = 0
  for i in range (len(magic_square)):
    sum_rl += magic_square[i][len(magic_square) - 1 - i]

 # Check sums
  if (sum_row != canon_sum or sum_column != canon_sum or sum_lr != canon_sum or sum_rl != canon_sum):
    return False
  else:
    return (sum_row, sum_column, sum_lr, sum_rl)

def main():

  print ()
 # Prompt the user to enter an odd number 3 or greater
  dimension = int (input ("Please enter an odd number: "))
  print ()

 # Check the user input
  while (dimension < 3 or dimension % 2 == 0):
    print ("Input is less than 3 or an even number", "\n")
    dimension = int (input ("Please enter an odd number: "))
    print()

 # Make and print the magic square
  magic_square = make_square (dimension)
  print_square (magic_square)
  print()

 # Verify that it is a magic square and print sums
  row, column, lr, rl = check_square (magic_square)
  print ("Sum of row = ", row)
  print ("Sum of column = ", column)
  print ("Sum of diagonal (UL to LR) = ", lr)
  print ("Sum of diagonal (UR to LL) = ", rl, "\n")
 
main()
