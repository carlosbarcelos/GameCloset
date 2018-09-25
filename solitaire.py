'''
@title Solitaire
@author Carlos Barcelos
@date TODO
'''
import tkinter  # GUI
import argparse # Command line arguments
import random   # Random seed

#####################
## Card Deck Class ##
#####################
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.data = "%s:%s" % (self.suit, self.value)

    def __repr__(self):
        return "%s:%s" % (self.suit, self.value)
    def __str__(self):
        return "%s:%s" % (self.suit, self.value)
    def __getitem__(self, k):
        return self

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

################
## Game Class ##
################

class Game:
    def __init__(self, drawNum):
        self.drawNum = drawNum
        # Stock pile to draw from
        self.stock = Deck().deck
        #TODO self.stock.shuffle()
        # Waste pile to play from
        self.waste = []
        # Four foundation, goal areas to build on
        self.foundation = [[],[],[],[]]
        # Seven tableau piles to build on
        self.tableau = [[],[],[],[],[],[],[]]

    def playerAction(self):
        action = input('Draw | ')

    def display(self):
        printString = ''
        for c in self.waste:
            printString += (c.data + ', ')
        printString += '\n'

        for row in self.foundation:
            for c in row:
                printString += ('F: ' + c.data + ', ')
            printString += '\n'
        printString += '\n'

        for row in self.tableau:
            for c in row:
                printString += ('T: ' + c.data + ', ')
            printString += '\n'
        printString += '\n'

        print(printString)

    def draw(self):
        if len(self.stock) <= 0:
            self.stock = self.mylist[::-1]
            self.waste = []
        for i in range(self.drawNum):
            c = self.stock.pop()
            self.waste.append(c)

    def isValid(self):
        return True

    def isGameOver(self):
        return False
####################
## End Game Class ##
####################

###############
## Main Loop ##
###############
def main(args):
    g = Game(args.draw)
    while(not g.isGameOver):
        g.display()
        g.playerAction()
        print('PAUSED. Need to develop GUI')
    return 0 # Success
##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='Solitaire. A card game without cards')

# Determine the number of cards per draw
parser.add_argument('--draw', dest='draw', type=int, default=3,
                    help='The number of cards in a draw')

# TODO Handle multiple decks

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    main(args)
