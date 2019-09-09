#  File: CalculatePI.py

#  Description: Compute PI using monte Carlos method, then compare outcome to PI

#  Date Created: 12 October 2017

#  Date Last Modified: 17 October 2017

import math
import random

# create function to compute PI
def computePI (numThrows): 
   
 # variables to count throws inside both circle and square or only square
  circleArea = 0
  squareArea = 0
    
 # find number of times a random throw lands in circle area
  while (squareArea < numThrows):

   # variables representing X and Y coordinates
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    if (math.hypot(xPos, yPos) < 1.0):
      circleArea += 1
    squareArea += 1

 # variable representing ratio of throws inside circle to throws inside square
  PI = 4.0 * circleArea / squareArea
  return PI

def main ():

 # beginning spacers and introduction text
  print ("")
  print ("Computation of PI using Random Numbers")
  print ("")
 
 # loop to iterate through each trial
  for numThrows in [100, 1000, 10000, 100000, 1000000, 10000000]:
    calculatedPI = computePI(numThrows)
    diff = calculatedPI - math.pi

   # print data
    print ("num =", format(numThrows, "<8d"), end = "    ")
    print ("Calculated PI =", format(calculatedPI, "8.6f"), end = "    ")
    print ("Difference = ", format(diff, "<+8.6f"))

 # end spacers and note to user
  print ("")
  print("Difference = Calculated PI - math.pi")
  print ("")
  
main ()

