#  File: GuessingGame.py

#  Description: Guesses user number within seven tries using binary search

#  Date Created: 13 November 2017

#  Date Last Modified: 15 November 2017

def main ():

 # heading and description comment to user
  print ("\nGuessing Game\n")
  print ("Think of a number between 1 and 100 inclusive.")
  print ("And I will guess what it is in 7 tries or less.\n")
 # setting variables and confirming that the user is prepared
  guess = 0
  lo = 1
  hi = 100
  play = input ("Are you ready? (y/n): ")
  print ("")
 # binary search to find user's number
  while (play == "y"):
    guess += 1
    mid = (lo + hi) // 2
    if (mid == 0):
      mid += 1
   # adjust range based on user input
    print ("Guess ", guess, ":", "The number you thought was ", mid)
    result = int (input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
    print ("")
    if (guess > 6):
      print ("Either you guessed a number out of range or you had an incorrect entry.\n")
      break
    if (result == 0):
      break
    elif (result == 1):
      hi = mid - 1
    else:
      lo = mid + 1
 # closing comment
  print ("Thank you for playing the Guessing Game.\n")

main ()
