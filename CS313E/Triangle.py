#  File: Triangle.py

#  Description: finds the largest path sum of a triangle using exhaustive search,
#  greedy search, divide and conquer, and dynamic programming. Then compares the 
#  outcomes and runtime.

#  Date Created: 06 March 2018

#  Date Last Modified: 09 March 2018

import time

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):

  num_lines = len(grid)
  num_solutions = 2 ** (num_lines - 1)
  maximum = 0

  for row in range(num_solutions):
    temp = int(grid[0][0])
    idx = 0 
    for col in range(num_lines - 1):
      idx = idx + (row >> col & 1)
      temp += int(grid[col + 1][idx])
    if temp > maximum:
      maximum = temp

  return maximum

# returns the greatest path sum using greedy approach
def greedy (grid):

  grid_sum = 0
  row_high = 0
  prev = 0

  for row in grid:
    if len(row) > 1:
      if row[prev] > row[prev + 1]:
        row_high = row[prev]
      else:
        row_high = row[prev + 1]
        prev += 1
    else:
      row_high = row[0]
    grid_sum += row_high

  return grid_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid, row, col):

  num_rows = len(grid)

  if row >= num_rows:
    return 0
  else:
    adj1 = rec_search(grid, row + 1, col)
    adj2 = rec_search(grid, row + 1, col + 1)
    fin = max(adj1, adj2) + int(grid[row][col])

  return fin

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):

  num_lines = len(grid)

  for row in range(num_lines - 2, -1, -1):
    for col in range(row + 1):
      grid[row][col] = int(grid[row][col]) + max(int(grid[row+1][col]), int(grid[row+1][col+1]))
  val = grid[0][0]
  triangle = grid

  return val, triangle

# reads the file and returns a 2-D list that represents the triangle
def read_file ():

  rows = []

  with open ("triangle.txt", "r") as in_file:
    n = int (in_file.readline ())
    for line in in_file:
      row = line.rstrip().split()
      row = [int (i) for i in row]
      rows.append (row)

  return n, rows

def main ():

  # read triangular grid from file
  n, rows = read_file()
  print()
  
  ti = time.time ()
  # output greatest path from exhaustive search
  final = exhaustive_search(rows)
  tf = time.time ()
  del_t = tf - ti
  print ("The greatest path sum through greedy search is {}.".format(final))
  # print time taken using exhaustive search
  print ("The time taken for exhaustive search is {} seconds.".format(del_t))
  print()
  
  ti = time.time()
  # output greatest path from greedy approach
  final = greedy(rows)
  tf = time.time()
  del_t = tf - ti
  print ("The greatest path sum through greedy search is {}.".format(final))
  # print time taken using greedy approach
  print ("The time taken for greedy approach is {} seconds.".format(del_t))
  print()

  ti = time.time()
  # output greatest path from divide-and-conquer approach
  final = rec_search(rows, 0, 0)
  tf = time.time()
  del_t = tf - ti
  print ("The greatest path sum through divide and conquer is {}.".format(final))
  # print time taken using divide-and-conquer approach
  print ("The time taken for recursive search is {} seconds.".format(del_t))
  print()
  
  ti = time.time()
  # output greatest path from dynamic programming 
  final, grid = dynamic_prog(rows)
  tf = time.time()
  del_t = tf - ti
  print ("The greatest path sum through dynamic programming is {}.".format(final))
  # print time taken using dynamic programming
  print ("The time taken for dynamic programming is {} seconds.".format(del_t))
  print()

if __name__ == "__main__":
  main()
  
