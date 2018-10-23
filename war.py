'''
@title War
@author Carlos Barcelos
@V1: 5/19/2015
@V2: 10/19/2018
'''

from random import shuffle
import time

##################
## Player Class ##
##################
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    # Return a list of n cards from the hand
    def getCards(self, n):
        loc = []
        try:
            for i in range(n):
                loc = [self.hand.pop()] + loc
        # If no more cards, return what you have
        except IndexError: pass
        return loc

    # Add a list of n cards to the hand
    def takeCards(self, loc):
        cnt = len(loc)
        for i in range(cnt):
            self.hand = self.hand + [loc[i]]

######################
## End Player Class ##
######################

################
## Game Class ##
################
class Game():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.pot = [[],[]]
        self.round = 0

    # Deal a fresh new hand to both players
    def deal(self):
        # Aces low
        suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        deck = suit * 4
        shuffle(deck)

        self.p1.hand = deck[0:len(deck)//2]
        self.p2.hand = deck[len(deck)//2:len(deck)]

    # Play a hand with n cards
    def play(self, n):
        self.round += 1
        print(f'Round {self.round}')

        # Put the cards on the table
        self.pot[0] += self.p1.getCards(n)
        self.pot[1] += self.p2.getCards(n)
        print(f'P1: {self.pot[0]}  |  {self.pot[1]} :P2')

        # Player 1 wins this round
        if self.pot[0][-1] > self.pot[1][-1]:
            self.p1.takeCards(self.pot[0]+self.pot[1])
            print(f'{self.p1.name} wins the round')
        # Player 2 wins this round
        elif self.pot[0][-1] < self.pot[1][-1]:
            self.p2.takeCards(self.pot[0]+self.pot[1])
            print(f'{self.p2.name} wins the round')
        # There is a tie
        else:
            print('WAR. Moving to tie breaker.')
            return self.play(3)

        # Report the results of the round
        print(f'{self.p1.name} hand : {len(self.p1.hand)}')
        print(f'{self.p2.name} hand : {len(self.p2.hand)}')
        print('**********')
        self.pot = [[],[]]
        return

    # Return the winning player
    def getWinner(self):
        if len(self.p1.hand) == 0:
            return self.p2.name
        elif len(self.p2.hand) == 0:
            return self.p1.name
        else:
            return None
####################
## End Game Class ##
####################

# Main function
def main():
    start = time.time()
    # Setup
    p1 = Player('P1')
    p2 = Player('P2')
    g = Game(p1, p2)
    g.deal()
    # Play the game
    while g.getWinner() is None:
        g.play(1)
    # Report the results
    print(f'{g.getWinner()} wins!')
    print('This game took {0:.3f} seconds to play'.format(time.time() - start,3))

# Run Main
if __name__ == '__main__':
    main()
