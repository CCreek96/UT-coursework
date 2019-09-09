#  File: Poker.py

#  Description: Simulate a game of five-card draw poker using object
#  oriented programming

#  Date Created: 05 February 2018

#  Date Last Modified: 10 February 2018

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_hand):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_hand):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hand of each player and print
    for i in range (len(self.players)):
      sorted_hand = sorted (self.players[i], reverse = True)
      self.players[i] = sorted_hand
      hand = ''
      for card in sorted_hand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

  def compare(self):
    # sort 
    for i in range(len(self.players)):
      self.players[i] = sorted(self.players[i],reverse = True)
    # evaluate hand and store the value
      catagory = []
      winnerList = []
      for hand in self.players:
        if self.is_royal(hand):
          catagory.append(10)
        elif self.is_straight_flush(hand):
          catagory.append(9)
        elif self.is_four_kind(hand):
          catagory.append(8)
        elif self.is_full_house(hand):
          catagory.append(7)
        elif self.is_flush(hand):
          catagory.append(6)
        elif self.is_straight(hand):
          catagory.append(5)
        elif self.is_three_kind(hand):
          catagory.append(4)
        elif self.is_two_pair(hand):
          catagory.append(3)
        elif self.is_one_pair(hand):
          catagory.append(2)
        elif self.is_high_card(hand):
          catagory.append(1)

    # print the hand:
    for i in range(len(catagory)):
      if catagory[i] == 10:
        print("Hand " + str(i+1) + ": Royal Flush")
      elif catagory[i] == 9:
        print("Hand " + str(i+1) + ": Straight Flush")
      elif catagory[i] == 8:
        print("Hand " + str(i+1) + ": Four of a Kind")
      elif catagory[i] == 7:
        print("Hand " + str(i+1) + ": Full House")
      elif catagory[i] == 6:
        print("Hand " + str(i+1) + ": Flush")
      elif catagory[i] == 5:
        print("Hand " + str(i+1) + ": Straight")
      elif catagory[i] == 4:
        print("Hand " + str(i+1) + ": Three of a Kind")
      elif catagory[i] == 3:
        print("Hand " + str(i+1) + ": Two Pair")
      elif catagory[i] == 2:
        print("Hand " + str(i+1) + ": One Pair")
      elif catagory[i] == 1:
        print("Hand " + str(i+1) + ": High Card")
    print()
          
    # compare the catagory of the hand
    catagorySorted = sorted(catagory);
    maxcatagory = catagorySorted[len(catagorySorted)-1]
    tie_breaker_list = []
    for i in range(len(catagory)):
      if catagory[i] == maxcatagory:
        tie_breaker_list.append(i)

    # print the winner if there is no tie
    if len(tie_breaker_list) == 1:
      print("Hand " + str(tie_breaker_list[0]+1) + " wins.")
    # do the tiebreak if there is a tie
    # there is no tiebreak for royal flush
    elif maxcatagory == 10:
      for i in tie_breaker_list:
        print("Hand " + str(i+1) + " ties.")
    # tiebreak for other cases
    else:
      maxHand = self.players[tie_breaker_list[0]]      
      winnerList = [tie_breaker_list[0]]                # a list that contains the indexes of winners 
      for i in range(1,len(tie_breaker_list)):
        hand1 = maxHand
        hand2 = self.players[tie_breaker_list[i]]
        winner = 0
              
        if maxcatagory == 9:
          winner = self.straight_flush_tie_breaker(hand1,hand2)
        elif maxcatagory == 8:
          winner = self.four_tie_breaker(hand1,hand2)
        elif maxcatagory == 7:
          winner = self.full_tie_breaker(hand1,hand2)
        elif maxcatagory == 6:
          winner = self.flush_tie_breaker(hand1,hand2)
        elif maxcatagory == 5:
          winner = self.straight_tie_breaker(hand1,hand2)
        elif maxcatagory == 4:
          winner = self.three_tie_breaker(hand1,hand2)
        elif maxcatagory == 3:
          winner = self.two_tie_breaker(hand1,hand2)
        elif maxcatagory == 2:
          winner = self.one_tie_breaker(hand1,hand2)
        elif maxcatagory == 1:
          winner = self.high_tie_breaker(hand1,hand2)
                  
        if winner == 2:
          maxHand = hand2      
          winnerList = [tie_breaker_list[i]]  
        elif winner == 0:
          winnerList.append(tie_breaker_list[i])  

    # print the winner
    if (len(winnerList) == 1):
      print("Hand " + str(winnerList[0]+1) + " wins.")
    else:
      for i in winnerList:
        print("Hand " + str(i+1) + " ties.")

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return False
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    return (same_suit and rank_order)
 
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return False
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i + 1].rank)
    return (same_suit and rank_order)

  def straight_flush_tie_breaker (self, hand1, hand2):
    if hand1[0] > hand2[0]:
      return 1
    elif hand1[0] < hand2[0]:
      return 2
    else:
      return 0

  def is_four_kind (self, hand):
    occurence = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        occurence += 1
    return (occurence == 4)

  def four_tie_breaker (self,hand1,hand2):
    if hand1[0] == hand1[1]:
      hand1Rank = hand1[0].rank
    else:
      hand1Rank = hand1[len(hand1)-1].rank    
    if hand2[0] == hand2[1]:
      hand2Rank = hand2[0].rank
    else:
      hand2Rank = hand2[len(hand2)-1].rank
    if hand1Rank > hand2Rank:
      return 1
    elif hand1Rank < hand2Rank:
      return 2
    else:
      return 0

  def is_full_house (self, hand):
    if (hand[0] == hand[1] and hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[3] and hand[3] == hand[4]):
      return True   
    else:
      return False

  def full_tie_breaker (self, hand1, hand2):
    if hand1[1] == hand1[2] and hand1[1] == hand1[0]:
      hand1Rank = hand1[0].rank
    else:
      hand1Rank = hand1[4].rank
    if hand2[1] == hand2[2] and hand2[1] == hand2[0]:
      hand2Rank = hand2[0].rank
    else:
      hand2Rank = hand2[4].rank
    if hand1Rank > hand2Rank:
      return 1
    elif hand1Rank < hand2Rank:
      return 2
    else:
      return 0

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return False
    else: 
      return True

  def flush_tie_breaker (self, hand1, hand2):
    if hand1[0] > hand2[0]:
      return 1
    elif hand1[0] < hand2[0]:
      return 2
    else:
      return 0

  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i + 1].rank)

  def straight_tie_breaker (self, hand1, hand2):
    if hand1[0] > hand2[0]:
      return 1
    elif hand1[0] < hand2[0]:
      return 2
    else:
      return 0

  def is_three_kind (self, hand):
    occurence = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        occurence += 1
    return (occurence == 3)

  def three_tie_breaker (self,hand1,hand2):
    if hand1[0] == hand1[1] and hand1[1] == hand1[2]:
      hand1rank = hand1[0].rank
    if hand1[1] == hand1[2] and hand1[2] == hand1[3]:
      hand1rank = hand1[1].rank
    if hand1[2] == hand1[3] and hand1[3] == hand1[4]:
      hand1rank = hand1[2].rank
         
    if hand2[0] == hand2[1] and hand2[1] == hand2[2]:
      hand2rank = hand2[0].rank
    if hand2[1] == hand2[2] and hand2[2] == hand2[3]:
      hand2rank = hand2[1].rank
    if hand2[2] == hand2[3] and hand2[3] == hand2[4]:
      hand2rank = hand2[2].rank
  
    if hand1rank > hand2rank:
      return 1
    elif hand1rank < hand2rank:
      return 2
    else:
      return 0

  def is_two_pair (self, hand):
    if hand[0] == hand[1] and hand[2] == hand[3]:
      return True
    if hand[0] == hand[1] and hand[3] == hand[4]:
      return True
    if hand[1] == hand[2] and hand[3] == hand[4]:
      return True
    return False

  def two_tie_breaker (self,hand1,hand2):
    # find the highest pair then the second highest pair then the fifth card for hand1
    if hand1[0] == hand1[1] and hand1[2] == hand1[3]:
      if (hand1[0] > hand1[2]):
        hand1rank1 = hand1[0].rank
        hand1rank2 = hand1[2].rank
      else:
        hand1rank1 = hand1[2].rank
        hand1rank2 = hand1[0].rank
      hand1rank3 = hand1[4].rank
          
    elif hand1[0] == hand1[1] and hand1[3] == hand1[4]:
      if hand1[0] > hand1[3]:
        hand1rank1 = hand1[0].rank
        hand1rank2 = hand1[3].rank
      else:
        hand1rank1 = hand1[3].rank
        hand1rank2 = hand1[0].rank
      hand1rank3 = hand1[2]
              
    else:
      if hand1[1] > hand1[3]:
        hand1rank1 = hand1[1].rank
        hand1rank2 = hand1[3].rank
      else:
        hand1rank1 = hand1[3].rank
        hand1rank2 = hand1[1].rank
      hand1rank3 = hand1[0].rank

    # find the highest pair then the second highest pair then the fifth card for hand2
    if hand2[0] == hand2[1] and hand2[2] == hand2[3]:
      if (hand2[0] > hand2[2]):
        hand2rank1 = hand2[0].rank
        hand2rank2 = hand2[2].rank
      else:
        hand2rank1 = hand2[2].rank
        hand2rank2 = hand2[0].rank
      hand2rank3 = hand2[4].rank
          
    elif hand2[0] == hand2[1] and hand2[3] == hand2[4]:
      if hand2[0] > hand2[3]:
        hand2rank1 = hand2[0].rank
        hand2rank2 = hand2[3].rank
      else:
        hand2rank1 = hand2[3].rank
        hand2rank2 = hand2[0].rank
      hand2rank3 = hand2[2]
              
    else:
      if hand2[1] > hand2[3]:
        hand2rank1 = hand2[1].rank
        hand2rank2 = hand2[3].rank
      else:
        hand2rank1 = hand2[3].rank
        hand2rank2 = hand2[1].rank
      hand2rank3 = hand2[0].rank

    # start comparison 
    if hand1rank1 > hand2rank1:
      return 1
    elif hand1rank1 == hand2rank1:
      if hand1rank2 > hand2rank2:
        return 1
      elif hand1rank2 == hand2rank2:
        if hand1rank3 > hand2rank3:
          return 1
        elif hand1rank3 == hand2rank3:
          return 0
        else:
          return 2
      else:
        return 2
    else:
      return 2

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False

  def one_tie_breaker (self,hand1,hand2):
    # find the rank for the pair then the highest side card then second highest then third highest
    if hand1[0] == hand1[1]:
      h1r1 = hand1[0].rank
      h1r2 = hand1[2].rank
      h1r3 = hand1[3].rank
      h1r4 = hand1[4].rank

    elif hand1[1] == hand1[2]:
      h1r1 = hand1[1].rank
      h1r2 = hand1[0].rank
      h1r3 = hand1[3].rank
      h1r4 = hand1[4].rank

    elif hand1[2] == hand1[3]:
      h1r1 = hand1[2].rank
      h1r2 = hand1[0].rank
      h1r3 = hand1[1].rank
      h1r4 = hand1[4].rank

    elif hand1[3] == hand1[4]:
      h1r1 = hand1[3].rank
      h1r2 = hand1[0].rank
      h1r3 = hand1[1].rank
      h1r4 = hand1[2].rank

    # second hand
    if hand2[0] == hand2[1]:
      h2r1 = hand2[0].rank
      h2r2 = hand2[2].rank
      h2r3 = hand2[3].rank
      h2r4 = hand2[4].rank

    elif hand2[1] == hand2[2]:
      h2r1 = hand2[1].rank
      h2r2 = hand2[0].rank
      h2r3 = hand2[3].rank
      h2r4 = hand2[4].rank

    elif hand2[2] == hand2[3]:
      h2r1 = hand2[2].rank
      h2r2 = hand2[0].rank
      h2r3 = hand2[1].rank
      h2r4 = hand2[4].rank

    elif hand2[3] == hand2[4]:
      h2r1 = hand2[3].rank
      h2r2 = hand2[0].rank
      h2r3 = hand2[1].rank
      h2r4 = hand2[2].rank

    # start comparison
    if h1r1 > h2r1:
      return 1
    elif h1r1 < h2r1:
      return 2
    elif h1r2 > h2r2:
      return 1
    elif h1r2 < h2r2:
      return 2
    elif h1r3 > h2r3:
      return 1
    elif h1r3 < h2r3:
      return 2
    elif h1r4 > h2r4:
      return 1
    elif h1r4 < h2r4:
      return 2
    else:
      return 0

  def is_high_card (self, hand):
    return True

  def high_tie_breaker (self, hand1, hand2):
    if hand1[0] > hand2[0]:
      return 1
    elif hand1[0] < hand2[0]:
        return 2
    elif hand1[1] > hand2[1]:
      return 1
    elif hand1[1] < hand2[1]:
      return 2
    elif hand1[2] > hand2[2]:
      return 1
    elif hand1[2] < hand2[2]:
      return 2
    elif hand1[3] > hand2[3]:
      return 1
    elif hand1[3] < hand2[3]:
      return 2
    elif hand1[4] > hand2[4]:
      return 1
    elif hand1[4] < hand2[4]:
      return 2
    else:
      return 0

def main():
  # prompt user to enter the number of hand
  num_hand = int (input ('Enter number of players: '))
  while ((num_hand < 2) or (num_hand > 6)):
    num_hand = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_hand)

  # play the game and compare
  game.play()
  game.compare()

main()
