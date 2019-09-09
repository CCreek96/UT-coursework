
# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Date Created: 4/5/18

#  Date Last Modified: 4/7/28


class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    s = ''
    s += "(" + str(self.col) + ',' + str(data) + ")" + '\n'
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # return a String representation of a LinkedList
  def __str__ (self):
    current = self.first
    while current != None:
      s += "," + "(" + str(self.col) + "," + str(current.data) + ")"
      current = current.next
    return s

  def insert_link(self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link

    while (current.next.col != col):
      current = current.next

    current.next = new_link

  def delete_link(self, col, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.next.col != col and current.next.data != data):
      previous = current
      current = current.next

    previous.next = current.next

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    if (data == 0):
      self.deleteLink (row, col)
    else:
      self.insertLink (row, col, data)

  def finder (self, row, column):
    current = self.matrix.first
    while current != None:
      if current.col == col and current.row == row:
        return current
      current = current.next
    return None

  # add two sparse matrices
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return None

    mat = Matrix (self.row, self.col)
    for i in range (self.row):
      new_row = []
      for j in range (self.col):
        new_row.append (self.finder(i, j) + other.set_element(i, j))
      mat.matrix.append (new_row)

    return mat

  # multiply two sparse matrices
  def __mul__ (self, other):
    if (self.col != other.row):
      return None

    mat = Matrix (self.row, other.col)
    for i in range (self.row):
      new_row = []
      for j in range (other.col):
        sum_mult = 0
        for k in range (other.row):
          sum_mult += self.set_element(i, k) * other.set_element(k, j)
        new_row.append (sum_mult)
      mat.matrix.append (new_row)
    return mat

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    row_list = []
    current = self.matrix[n].first
    for j in range(self.col):
      if (current == None):
        row_list.append(0)
      elif (j == current.col):
        row_list.append(current.data)
        current = current.next
      else:
        row_list.append(0)
    return row_list

  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    col_list = []
    for row in self.matrix:
      current = row.first
      while (current != None):
        if (current.col == n):
          col_list.append(current.data)
          break
        current = current.next
      if (current == None):
        col_list.append(0)
    return col_list

  # return a String representation of a matrix
  def __str__ (self):
    s = ''
    for row in self.matrix:
      current = row.first
      for j in range(self.col):
        if (current == None):
          s += '%-4s ' % (0)
        elif (j == current.col):
          s += '%-4s ' % (current.data)
          current = current.next
        else:
          s += '%-4s ' % (0)
      s += '\n'
    return s

def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  
  in_file.close()

main()
