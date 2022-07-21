#  File: Poker.py

#  Description: Program to play poker and calculate winning hands from multiple
#  of players using a points system. Card is assumed to be 52 cards with the basic ranks 
#  and suits.

#  Student Name: Crystal Le

#  Student UT EID: 

#  Partner Name: Johnny Tran

#  Partner UT EID: JHT825

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 02/11/2022

#  Date Last Modified: 02/14/2022

from audioop import reverse
import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
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

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
    
    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand

    # test what type of hand the players have and append to list and
    # append points for that player as well
    for i in range(len(self.players_hands)):
      player = self.is_royal(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_straight_flush(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue


      player = self.is_full_house(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_four_kind(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_flush(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_straight(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_three_kind(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_two_pair(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_one_pair(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue

      player = self.is_high_card(self.players_hands[i])
      if player[0] != 0:
        hand_type.append(player[1])
        hand_points.append(player[0])
        continue 

    print()
    for i in range(len(hand_type)):
      print('Player ' + str(i + 1) + ': ' + hand_type[i])
    
    print()
    # determine winner and print
    tied = False
    winner = max(hand_points)
    result = False
    tied_player = 0
    tied_player2 = 0
    for i in range(len(hand_type)-1):
      if len(hand_type) > 0: 
        result = all(htype == hand_type[0] for htype in hand_type)
        if result == True:
          tied = True
          point_dict = {}
          # if there are multiple of ties
          for i in range(len(hand_points)):
            point_dict[hand_points[i]] = i + 1
          point_dict = sorted(point_dict.items(), reverse= True)
          for j in range(len(point_dict)):
            print('Player', point_dict[j][1] , 'ties.')
          break
        elif result == False:
          tied_player = i + 1
          tied_player2 = i + 2
          break

    # declared winner if no ties
    if (tied == False) or ((result == False) and \
        (tied == True) and (hand_points[tied_player] and hand_points[tied_player2] < winner)):
        for i in range(len(hand_points)):
          if hand_points[i] == winner:
            winner = i + 1
            print('Player', winner, 'wins.')
            break
    # declare ties
    elif (tied == True) and (result == False):
      if hand_points[tied_player] < hand_points[tied_player2]:
        print('Player', tied_player2, 'ties.')
        print('Player', tied_player, 'ties.')
      elif hand_points[tied_player] > hand_points[tied_player2]:
        print('Player',  tied_player, 'ties.')
        print('Player', tied_player2, 'ties.')
      else:
        print('Player',  tied_player, 'ties.')
        print('Player', tied_player2, 'ties.')
    


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and ((hand[i].rank - 1) == hand[i + 1].rank)

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
      
    return points, 'Straight Flush'
    
  def is_four_kind (self, hand):
    same_rank = False
    count = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        same_rank = True
        count += 1
      elif (hand[i].rank != hand[i + 1].rank):
        same_rank = False
        if i ==3:
          wrong_rank_idx = i+1
          wrong_rank = hand[i+1]
        else:
          wrong_rank_idx = i
          wrong_rank = hand[i]
    
    if (not same_rank) and count < 3:
      return 0, ''

    hand.pop(wrong_rank_idx)
    hand.append(wrong_rank)
    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Four of a Kind'

  def is_full_house (self, hand):
    same_rank = False
    count = 0
    hand.sort()
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        same_rank = True
        count+=1
      else:
        same_rank = False
        break
    # switch two pair hands to the end of the hand for points 
    if count == 1:
      hand[0], hand[3] = hand[3], hand[0]
      hand[1], hand[4] = hand[4], hand[1]
    
    elif count == 2:
      if hand[3].rank != hand[4].rank:
        count = 0

    if (not same_rank) and count < 1:
      return 0, ''

    points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Full House'

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
      if same_suit == False:
        break

    if (not same_suit):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
      
    return points, 'Flush'

  def is_straight (self, hand):
    rank_order = True
    diff_suit = []
    for i in range (len(hand) - 1):
      rank_order = rank_order and ((hand[i].rank - 1) == hand[i + 1].rank)
      if hand[i].suit not in diff_suit:
        diff_suit.append(hand[i].suit)

    if (not rank_order) and len(diff_suit) < 4:
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
      
    return points, 'Straight'

  def is_three_kind (self, hand):
    same_rank = False
    count = 0
    wrong_rank_idx = 0
    wrong_rank = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        same_rank = True
        count += 1
      elif (hand[i].rank != hand[i + 1].rank):
        same_rank = False
        if count == 2: 
          break
        else:
          if count <= 1:
            wrong_rank_idx = i
            wrong_rank = hand[i]
  
    
    if (not same_rank) and count < 2:
      return 0, ''
  
    # removing cards that are not part of the three kind to the end
    if wrong_rank or wrong_rank_idx != 0: 
      hand.pop(wrong_rank_idx)
      hand.append(wrong_rank)

    # reorder of cards to calculate cards
    if hand[3].rank < hand[4].rank:
      hand[4], hand[3] = hand[3], hand[4]
    
    points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Three of a Kind'

  def is_two_pair (self, hand):
    same_rank = False
    count = 0
    wrong_rank_idx = 0
    wrong_rank = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        same_rank = True
        count += 1
      elif (hand[i].rank != hand[i + 1].rank):
        same_rank = False
        if count == 2: 
          break
        else:
          if count <= 1:
            wrong_rank_idx = i 
            wrong_rank = hand[i]
  
    
    if (not same_rank) and count < 2:
      return 0, ''
    # removing non paired cards to the end
    if (wrong_rank or wrong_rank_idx != 0): 
      hand.pop(wrong_rank_idx)
      hand.append(wrong_rank)
    
    points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        hand[0], hand[i] = hand[i], hand[0]
        hand[1], hand[i+1] = hand[i+1], hand[1]
        break
    
    if (not one_pair):
      return 0, ''
    
    hand[2:5] = sorted(hand[2:5], reverse = True)

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'One Pair'

  def is_high_card (self,hand):
    # checking if the card is not any of of the other types of hands
    if (self.is_flush(hand) and self.is_four_kind(hand) and self.is_full_house(hand) \
        and self.is_one_pair(hand) and self.is_royal(hand) and self.is_straight(hand) and \
        self.is_straight_flush(hand) and self.is_three_kind(hand) and self.is_two_pair(hand)) == (0, ''):
      hand = sorted(hand, reverse = True)
    
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

def main():
  # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return

  # create the Poker object
    game = Poker (num_players)
  # play the game
    game.play()

if __name__ == "__main__":
  main()


