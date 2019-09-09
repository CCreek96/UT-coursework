#  File: Hailstone.py

#  Description: Puts out the number of cycles of the hailstone sequence in order to reduce a number to 1. 

#  Date Last Modified: 9/28/17

def main():

    StartNum, EndNum, maxlength = 0               
    maxnum = 1
        
    while (StartNum <= 0 and EndNum <= 0) and (StartNum >= EndNum):
        StartNum = int(input("Enter starting number of the range: "))       #Asking for input, check if valid
        EndNum = int(input("Enter ending number of the range: "))

    for i in range (StartNum, EndNum + 1):
        n = i
        count = 0
        while (n > 1):
            if (n%2 == 0):
                n = n//2                    #Algorithm
            elif (n%2 != 0):
                n = 3 * n + 1
            count += 1
            if (count > maxlength):
                maxlength = count
                maxnum = i
            if (count == maxlength) and (i > maxnum):
                maxnum = i
            
    print("The number", maxnum, "has the longest cycle length of", maxlength) #Final print statement


main()     
