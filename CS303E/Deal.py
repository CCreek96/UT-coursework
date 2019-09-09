#  File: CalculatePI.py

#  Description: Displays the probability of winning the Monty Hall game show by \
#  using a user defined number of trials

#  Date Created: 12 October 2017

#  Date Last Modified: 17 October 2017

from random import randint

def main():

   # prompt user for number of trials
    plays = int(input("\nEnter number of times you want to play: "))

   # print column headers
    print ("\n" "{:^10} {:^10} {:^10} {:^10}".format("Prize", "Guess", "View", "New Guess"))

   # run algorithm user defined number of times
    count = 0
    win_switch = 0
    while count < plays:

       # generate random number for necessary variables
        prize = randint(1, 3)
        guess = view = new_guess = randint(1, 3)
       # assign variables view and new_guess such that (view != prize or guess) and \
       # (new_guess != guess or view)
        while view == prize or view == guess:
            view = randint(1, 3)
        while new_guess == guess or new_guess == view:
            new_guess = randint(1, 3)

       # compare new guess to prize and count successes
        if new_guess == prize:
            win_switch += 1

       # print results of each trial 
        print ("{:5d} {:10d} {:10d} {:10d}".format(prize, guess, view, new_guess))
        count += 1
   # calculate and print the probability of winning with original guess or by switching 
    probability_win_switch = win_switch / plays
    probability_win_not_switch = 1 - probability_win_switch
    print ("\n" "Probability of winning if you switch = ", "{:.2f}".format(probability_win_switch))
    print ("Probability of winning if you do not switch = ", "{:.2f}".format(probability_win_not_switch), "\n")

main()
