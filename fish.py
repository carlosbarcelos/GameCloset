'''
@title Go Fish
@author Carlos Barcelos
@date 25 Sept. 2018
'''

import argparse # Command line arguments
import random   # Random seed

#####################
## Card Deck Class ##
#####################
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "%s:%s" % (self.suit, self.value)
    def __str__(self):
        return "%s:%s" % (self.suit, self.value)

    def isRed(self):
        return (self.suit == 'D') or (self.suit == 'H')

# Helper: Returns a standard, 52 card deck
def newDeck():
    returnDeck = []
    suits = ['S','H','C','D']
    for s in suits:
        # For numbered cards
        for i in range(2,11):
            returnDeck.append(Card(s, str(i)))
        # For lettered cards
        letters = ['J','Q','K','A']
        for l in letters:
            returnDeck.append(Card(s, l))
    return returnDeck

class Deck:
    def __init__(self):
        self.deck = newDeck()

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop(self):
        try:
            return self.deck.pop()
        except IndexError:
            return None

    def pushBottom(self, card):
        self.deck.append(card)

#########################
## End Card Deck Class ##
#########################

## Play Methods
# Manual Play
def manualPlay(p1, p2):
    if len(p1.hand) < 1:
        print('You have no cards to play.')
        return False

    ask = input('Do you have a > ')

    # p1 must have the card to ask for it
    if not any(ask in c.value for c in p1.hand):
        print('You must have the card to ask for it.')
        return manualPlay(p1, p2)

    if any(ask in c.value for c in p2.hand):
        matchedCards = [c for c in p2.hand if c.value == ask] # Get matched cards
        p2.hand = [c for c in p2.hand if not c.value == ask] # Remove from p2
        [p1.takeCard(c) for c in matchedCards] # Add to p1

        print('Good guess! Go again.')
        return manualPlay(p1, p2)
    else:
        print('Go Fish!\n')
        return False

# Random Play
def randomPlay(p1, p2):
    if len(p1.hand) < 1:
        print('You have no cards to play.')
        return False

    ask = random.choice(p1.hand).value

    if any(ask in c.value for c in p2.hand):

        matchedCards = [c for c in p2.hand if c.value == ask] # Get matched cards
        p2.hand = [c for c in p2.hand if not c.value == ask] # Remove from p2
        [p1.takeCard(c) for c in matchedCards] # Add to p1

        print('Good guess! Go again.')
        return randomPlay(p1, p2)
    else:
        print('Go Fish!\n')
        return False

##################
## Player Class ##
##################
def newHand(deck, numCards):
    returnHand = []
    for i in range(numCards):
        returnHand.append(deck.pop())
    return returnHand

def checkPair(p, card):
    pair = [c for c in p.hand if c.value == card.value] # Get matched cards
    if len(pair) == p.numMatch:
        p.hand = [c for c in p.hand if not c.value == card.value] # Remove from hand
        p.pairs.append(pair) # Add to pairs
        return True
    return False

class Player:
    def __init__(self, style, deck, numCards, numMatch):
        self.style = style
        self.pairs = []
        self.numMatch = numMatch
        self.hand = newHand(deck, numCards)

    def takeCard(self, card):
        if card == None:
            return False
        else:
            self.hand.append(card)
            checkPair(self, card)
            return True

    def displayHand(self):
        handString = '\n| '
        for c in self.hand:
            if self.style == 'manual':
                handString += (str(c) + ' | ')
            else:
                handString += ('*:* | ')
        print(handString)

    def displayPairs(self):
        pairString = 'PAIRS = '
        for p in self.pairs:
            pairString += (str(p) + ' | ')
        print(pairString)

    def ask(self, otherPlayer):
        styles = {
            'manual' : manualPlay,
            'random' : randomPlay,
        }
        return styles[self.style](self, otherPlayer)
######################
## End Player Class ##
######################

###############
## Main Loop ##
###############
def main(args):
    d = Deck()
    cardsLeft = len(d.deck)
    d.shuffle()

    p1 = Player('manual', d, args.cards, args.match)
    p2 = Player('random', d, args.cards, args.match)
    players = [p1,p2]

    # Check for any pre-delt pairs
    for p in players:
        for c in p.hand:
            checkPair(p, c)
    while(cardsLeft > 1):
        # Player 1
        p1.displayHand()
        p1.displayPairs()
        p1.ask(p2)
        p1.takeCard(d.pop())

        # Player 2
        p2.displayHand()
        p2.displayPairs()
        p2.ask(p1)
        p2.takeCard(d.pop())

        # Make sure there are enough cards for the next play
        cardsLeft = len(d.deck)
        for p in players:
            cardsLeft += len(p.hand)
    return 0
##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='Go Fish. A card game without cards')

# Determine the number of cards in each hand
parser.add_argument('--cards', dest='cards', type=int, default=7,
                    help='The number of cards in each hand')

# Determine the number of cards required to make a pair
parser.add_argument('--match', dest='match', type=int, default='2',
                    help='The number of cards in a pair (2 or 4)')

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    main(args)
