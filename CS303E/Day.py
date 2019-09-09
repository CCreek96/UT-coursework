#  File: Day.py

#  Description: Returns the day of the week when provided the year, month, and day

#  Date Created: 23 September 2017

#  Date Last Modified: 25 September 2017

def main():

  # prompt user for year, month, day

  a = int (input ("Enter Year: "))
  while (a < 1900) or (a > 2100):
    a = int (input ("Enter Year: "))
  

  month = int (input ("Enter Month: "))
  while (month < 1) or (month > 12):
    month = int (input ("Enter Month: "))
  if (month <= 2):
    month += 10
    a -= 1
  elif (month >= 3) or (month <= 10):
    month -= 2
  elif (month == 11) or (month == 12):
    month -= 10

  year = a % 100          # turns year into last two digits of year for formula
  century = a // 100      # turns year into first two digits of year for formula

  day = int (input ("Enter Day: "))

  while ((month == 11 or month == 1 or month == 3 or month == 5 or month == 6 or month == 8 or month == 10) and (day > 31 or day < 1)):
    day = int (input("Enter Day:"))
  while ((month == 2 or month == 4 or month == 7 or month == 9) and (day > 30 or day < 1)):
    day = int (input("Enter Day: "))
  while ((month == 2 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0) and (day > 29 or day < 1)):
    day = int (input("Enter Day: "))
  while ((month == 2 and year % 400 != 0 and year % 100 == 0 and year % 4 == 0) and (day > 28 or day < 1)):
    day = int (input ("Enter Day: "))


  # computation of Zeller's algorithm

  w = (13 * month - 1) // 5
  x = year // 4
  y = century // 4
  z = w + x + y + day + year - 2 * century
  r = z % 7
  r = (r + 7) % 7



# print results

  if(r == 0):
    print("The day is Sunday.")

  elif(r == 1):
    print("The day is Monday.")

  elif(r == 2):
    print("The day is Tuesday.")

  elif(r == 3):
    print("The day is Wednesday.")

  elif(r == 4):
    print("The day is Thursday.")

  elif(r == 5):
    print("The day is Friday.")

  elif(r == 6):
    print("The day is Saturday.")


main()
