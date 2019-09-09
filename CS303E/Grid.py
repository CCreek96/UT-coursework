
#  File: Grid.py

#  Description: returns the greatest product of four adjacent numbers in the same direction within a grid

#  Date Created: 01 November 2017

#  Date Last Modified: 02 November 2017

def main ():
  # open file for reading
  in_file = open ("./grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create an empty grid
  super_max = 0
  grid = []

  # populate the grid
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

  # close the file
  in_file.close()

  # read and multiply in blocks of four along rows
  for row in grid:
    for i in range (dim - 3):
      prod = 1
      for j in range (i, i + 4):
        prod = prod * row[j]
        if (prod > super_max):
          super_max = prod                 # set maximum product to variable super_max

  # read each column in blocks of four
  for j in range (dim):
    for i in range (dim - 3):
      prod = 1
      for k in range (i, i + 4):
        prod = prod * grid[k][j]
        if (prod > super_max):
          super_max = prod                # set maximum product to variable super_max

  # go along all diagonals L to R in blocks of 4
  for i in range (dim - 3):
    for j in range (dim - 3):
      prod = 1
      for k in range (4):
        prod = prod * grid[i + k][j + k]
        if (prod > super_max):
          super_max = prod                # set maximum product to variable super_max

  # go along all diagonals R to L in blocks of 4
  for i in range (dim - 3):
    for j in range (3, dim):
      prod = 1
      for k in range (4):
        prod = prod * grid[i + k][j - k]
        if (prod > super_max):
          super_max = prod                # set maximum product to variable super_max
  print ("The greatest product is", super_max)                       # print variable super_max

main ()
