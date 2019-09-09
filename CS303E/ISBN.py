#  File: ISBN.py

#  Description: read a text file containing ISBN codes and output whether the code is valid or invalid

#  Date Created: 29 October 2017

#  Date Last Modified: 30 October 2017


def main ():

 # validate ISBNs
  def valid (s1):

    for i in range (len(s1) - 1):
      if ((s1[i] == "x" or s1[i] == "X") or ((ord (s1[i]) < 48) or (ord (s1[i]) > 57))):
        return False
    if (len(s1) != 10):
        return False
    return True

  def is_isbn (s2):
 
    lst = []
    sum1 = []
    sum2 = 0
    while (valid (s2)):
      for i in range (len (s2)):
        if (s2[i] == "x" or s2[i] == "X" ):
          lst.append (10)
        else:
          lst.append (len (s2[i]))
      for j in range (len (lst)):
        if (j == 0):
      	  sum1.append (lst[0])
        else:
          sum1.append (lst[j] + sum1[j - 1])
      for k in range (len (sum1)):
        sum2 += sum1[k]

      if (sum2 % 11 == 0):
        return True
    return False
  
 # read textfile
  in_file = open ("./isbn.txt", "r")               # open infile
  outfile = open ("./output.txt", "w")             # open outfile
  for line in in_file:                             # read lines
    isbn = line.strip ().replace ("-","")
    if (valid (isbn) == True and is_isbn (isbn) == True):
      outfile.write (line.strip () + "  valid\n")
    else:
      outfile.write (line. strip () + "  invalid\n")
  in_file.close ()                                 # close in file 
  outfile.close ()                                 # close out file

main ()
