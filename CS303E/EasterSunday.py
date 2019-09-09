#  File: EasterSunday.py

#  Description: Compute the date of Easter Sunday for any given year

#  Date Created: 13 September 2017

#  Date Last Modified: 13 September 2017

def main ():

  # Prompt the user to enter a year 

  y = int (input ("Enter Year: "))

  # Compute easter sunday according to Gauss

  a = y % 19     # remainder a
  b = y // 100     # quotient  b
  c = y % 100     # remainder c
  d = b // 4     # quotient  d
  e = b % 4     # remainder e
  g = (8 * b + 13) // 25    # quotient  g
  h = (19 * a + b - d - g + 15) % 30   # remainder h
  j = c // 4      # quotient  j
  k = c % 4     # remainder k
  m = (a + 11 * h) // 319     # quotient  m
  r = (2 * e + 2 * j - k - h + m + 32) % 7     # remainder r
  n = (h - m + r + 90) // 25     # quotient  n
  p = (h - m + r + n + 19) % 32     # remainder p

  # Print the day and year

  print ()
  if (n == 3):
    print ("In", y, "Easter Sunday in on", p, "March.")
  if (n == 4):
    print ("In", y, "Easter Sunday is on", p, "April.") 

main ()
