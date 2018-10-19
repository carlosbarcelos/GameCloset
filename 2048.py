'''
@title 2048
@author Carlos Barcelos
@date 18 Oct. 2018
'''

import argparse # Command line arguments
import random   # Random seed

# TODO: Coordinates are tightly coupled. Make their own class
# TODO: Numbers currently combine in a chain as much as they can. Change to be more like 2048 rules.

#################
## Board Class ##
#################
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.emptySpace = '.'
        self.board = [[self.emptySpace for i in range(cols)] for j in range(rows)]

    # Display the game board
    def display(self):
        for rows in self.board:
            printString = ''
            for cols in rows:
                printString += (cols + '    ')
            print(printString+'\n')
        print()

    # Add cnt new numbers to the board in random positions
    def newNum(self, cnt):
        while(cnt > 0):
            if self.isFull(): return False

            n = random.choice([2,4])
            randI = random.randrange(self.rows)
            randJ = random.randrange(self.cols)
            if self.board[randI][randJ] == self.emptySpace:
                self.board[randI][randJ] = str(n)
                cnt -= 1

        return True

    # Move the pieces in a certain direction
    def move(self, dir):
        if dir == 'u':
            return self.moveUpDown(-1,0)
        elif dir == 'd':
            return self.moveUpDown(+1,0)
        elif dir == 'l':
            return self.moveLeftRight(0,-1)
        elif dir == 'r':
            return self.moveLeftRight(0,+1)
        else:
            return False

    # Helper to self.move()
    def moveUpDown(self, dI, dJ):
        validMove = False
        for n in range(self.rows):
            for i in range(self.rows-1, n-1, -1):
                for j in range(self.cols):
                    # Only run for non-empty spaces
                    if self.board[i][j] == self.emptySpace or\
                    self.isOutOfRange(i+dI,j+dJ):
                        continue

                    # If next space is empty, move to it
                    if self.board[i+dI][j+dJ] == self.emptySpace:
                        self.board[i+dI][j+dJ] = self.board[i][j]
                        self.board[i][j] = self.emptySpace
                        validMove |= True

                    # Else if, next space has value equal to this space value, combine
                    elif self.board[i][j] == self.board[i+dI][j+dJ]:
                        self.board[i+dI][j+dJ] = str(int(self.board[i][j])*2)
                        self.board[i][j] = self.emptySpace
                        validMove |= True
        return validMove

    # Helper to self.move()
    def moveLeftRight(self, dI, dJ):
        validMove = False
        for n in range(self.cols):
             for j in range(self.cols-1, n-1, -1):
                for i in range(self.rows):
                    # Only run for non-empty spaces
                    if self.board[i][j] == self.emptySpace or\
                    self.isOutOfRange(i+dI,j+dJ):
                        continue

                    # If next space is empty, move to it
                    if self.board[i+dI][j+dJ] == self.emptySpace:
                        self.board[i+dI][j+dJ] = self.board[i][j]
                        self.board[i][j] = self.emptySpace
                        validMove |= True

                    # Else if, next space has value equal to this space value, combine
                    elif self.board[i][j] == self.board[i+dI][j+dJ]:
                        self.board[i+dI][j+dJ] = str(int(self.board[i][j])*2)
                        self.board[i][j] = self.emptySpace
                        validMove |= True
        return validMove

    # Helper: Determines if the (i,j) corrdinate is out of the boards range
    def isOutOfRange(self, i, j):
        res = False
        if (i < 0) or (i >= self.rows):
            res = True
        if (j < 0) or (j >= self.cols):
            res = True
        return res

    # Determine if the game board is full and cannot accept new tiles
    def isFull(self):
        for row in self.board:
            for col in row:
                if col == self.emptySpace:
                    return False
        return True

#####################
## End Board Class ##
#####################

# Determine if a direction input is is valid
def isValidDir(dir):
    return dir in ['u','d','l','r']

###############
## Main Loop ##
###############
def main(args):
    b = Board(args.rows, args.cols)
    b.newNum(2)

    while(not b.isFull()):
        b.display()
        dir = None
        while (not isValidDir(dir)):
            dir = input('> ')
        if (not b.move(dir)):
            print('Invalid Move')
            continue
        b.newNum(1)

    print('Game Over. Board is full.')

##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='2048. Combine the numbers. With numbers!')

# Determine the size of the board
parser.add_argument('--rows', dest='rows', type=int, default='4',
                    help='The number of rows in the board')
parser.add_argument('--cols', dest='cols', type=int, default='4',
                    help='The number of columns in the board')

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    main(args)
