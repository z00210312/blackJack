# this program is writen by Jia Shin Tseng::tz4862
# this program last modified in Jan 18 2018
# the purpose for this program is to demonstrate functions of BlackJack

# hand-related constants
CARDS_PER_HAND = 2
# exception when there are no enough cards
class TooFewCardsError(Exception):
    " Too few cards to complete the deal for all players "
    pass
# disturbute the card in the deck
def deal(deck, hands):
  deck.reverse()
  setHands(hands)
  nhands = len(hands)
  if (len(deck) < (CARDS_PER_HAND * nhands)):
    raise TooFewCardsError
  for card in range (0,CARDS_PER_HAND):
    for hand in hands:
      hand.append(deck.pop())
      del hand[0]
  return hands
# return the score
def score(hand):
  newValue = 0
  numOfAce = 0
  for card in hand:
    if card[0] == 1:
      numOfAce += 1
      newValue += 11
    elif card[0] >= 10:
      newValue += 10
    else:
      newValue += card[0]
    if((newValue > 21) & (numOfAce > 0)):
      numOfAce -= 1
      newValue -= 10
    elif(newValue > 21):
      break
  return newValue
# draw cards from the deck
def draw(deck, hands):
  for index in range (0,len(hands)):
    hands[index].append(deck.pop())
  return hands
# initlize the empty hands to proper tuples
def setHands(hands):
  for hand in hands:
    for card in range (0,CARDS_PER_HAND-len(hand)):
      hand.append(tuple())
# show result of hands
def playersScore(hands):
  for index in range (0,len(hands)):
    if(score(hands[index]) == 21):
      print('Player',(index+1),'got BlackJack')
    elif(score(hands[index]) > 21):
      print('Player',(index+1),'got',score(hands[index]), 'lose the game')
    else:
      print('Player',(index+1),'got',score(hands[index]))
      
# the purpose for this class is to do the testing of BlackJack's functions
import unittest
class TestBlackJackFns(unittest.TestCase):
  # if the deck has perfect fit
  def test_deal_fit(self):
    deck = [(2, 'Clubs'), (10, 'Hearts'), (9, 'Spades'), (8, 'Diamonds')]
    deal(deck, ([],[]))
    assert (len(deck) == 0),"perfect fit"
  # if the deck has few cards
  def test_deal_few(self):
    deck = [(2, 'Clubs'), (10, 'Hearts'), (9, 'Spades'), (8, 'Diamonds')]
    with self.assertRaises(TooFewCardsError):
      deal(deck, ([],[],[]))
  # if the deck has more cards
  def test_deal_more(self):
    deck = [(2, 'Clubs'), (10, 'Hearts'), (9, 'Spades'), (8, 'Diamonds'), (2, 'Clubs'), (10, 'Hearts'), (9, 'Spades'), (8, 'Diamonds')]
    hands = ([],[])
    deal(deck, hands)
    assert (len(deck) == (len(hands)*(len(hands[0])))),"too much cards"
  # if the score is 10
  def test_score_case1(self):
    assert(score([(2, 'Clubs'),(8, 'Diamonds')]) == 10),"It is not 10"
  # if the score is 20
  def test_score_case2(self):
    assert(score([(13, 'Clubs'),(11, 'Diamonds')]) == 20),"It is not 20"
  # if the score is 12
  def test_score_case3(self):
    assert(score([(1, 'Clubs'),(1, 'Diamonds')]) == 12),"It is not 12"    
if __name__ == '__main__':
  unittest.main()
