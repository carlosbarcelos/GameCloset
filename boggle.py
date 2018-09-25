'''
@title Boggle
@author Carlos Barcelos
@date 24 Sept. 2018
'''

import argparse # Command line arguments
import random   # Random seed

################
## Dice Class ##
################
d0 = ['R','I','F','O','B','X']
d1 = ['I','F','E','H','E','Y']
d2 = ['D','E','N','O','W','S']
d3 = ['U','T','O','K','N','D']
d4 = ['H','M','S','R','A','O']
d5 = ['L','U','P','E','T','S']
d6 = ['A','C','I','T','O','A']
d7 = ['Y','L','G','K','U','E']
d8 = ['Qu','B','M','J','O','A']
d9 = ['E','H','I','S','P','N']
d10 = ['V','E','T','I','G','N']
d11 = ['B','A','L','I','Y','T']
d12 = ['E','Z','A','V','N','D']
d13 = ['R','A','L','E','S','C']
d14 = ['U','W','I','L','R','G']
d15 = ['P','A','C','E','M','D']

# Get the dice for this sized Board
def getDice():
    return [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]
####################
## End Dice Class ##
####################

#################
## Board Class ##
#################
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['-' for i in range(size)] for j in range(size)]

    # Populate the board with the give list of dice
    def populate(self, lod):
        for i in range(self.size):
            for j in range(self.size):
                die = lod.pop(random.randrange(0,len(lod)))
                self.board[i][j] = die.pop(random.randrange(0,len(die)))

    # Display the contents of the board
    def display(self):
        for rows in self.board:
            printString = ''
            for cols in rows:
                printString += (cols + ' ')
            print(printString)
#####################
## End Board Class ##
#####################

###############
## Main Loop ##
###############
def main(args):
    lod = getDice()
    b = Board(4)
    b.populate(lod)
    b.display()
    return 0 # Success
##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='Boggle. The dice game without dice.')

# Deterministic game seed
parser.add_argument('--seed', dest='seed', type=int, default=None,
                    help='The seed value for this game')

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    random.seed(args.seed)
    main(args)
