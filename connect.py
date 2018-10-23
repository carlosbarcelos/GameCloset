'''
@title Connect N
@author Carlos Barcelos
@date 24 Sept. 2018
'''

from os import system
import argparse # Command line arguments
import random   # Random seed

#################
## Board Class ##
#################
# Helper: Recursivly get the number of pieces in a row
def isConnected(board, i, j, dI, dJ, piece):
    try:
        if board[i][j] == piece:
            return isConnected(board, i+dI, j+dJ, dI, dJ, piece) + 1
        else:
            return 0
    except IndexError:
        return 0

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.emptySpace = '-'
        self.board = [[self.emptySpace for i in range(cols)] for j in range(rows)]

    def isWinner(self, piece, connect):
        for i in range(self.rows):
            for j in range(self.cols):
                if isConnected(self.board, i, j, 1, 0, piece) >= 4:
                    return True # Down Connected
                if isConnected(self.board, i, j, 0, 1, piece) >= 4:
                    return True # Right Connected
                if isConnected(self.board, i, j, 1, 1, piece) >= 4:
                    return True # Down-Right Connected
                if isConnected(self.board, i, j, 1, -1, piece) >= 4:
                    return True # Down-Left Connected
        return False

    def isFull(self):
        for rows in self.board:
            for cols in rows:
                if cols == self.emptySpace:
                    return False
        return True

    def display(self):
        # Clear the screen and display the current game board
        system('cls')
        for rows in self.board:
            printString = ''
            for cols in rows:
                printString += (cols + ' ')
            print(printString)

        colNumbers = ''
        for j in range(self.cols):
            colNumbers += (str(j) + ' ')
        print(colNumbers+'\n')

    def addToCol(self, col, piece):
        for i in range(self.rows-1,-1,-1):
            if self.board[i][col] == self.emptySpace:
                self.board[i][col] = piece
                return True
            else:
                continue
        return False
#####################
## End Board Class ##
#####################

## Play Methods
# Manual Play
def manualPlay(board, piece):
    try:
        col = int(input(piece + ': Place a piece in which row? '))

        # The input must be in the range of the board
        if (col < 0) or (col > board.rows):
            print('That column is not within the range of the board. Try again.')
            return manualPlay(board, piece)
        # The column must not be full
        if board.addToCol(col, piece):
            return True
        else:
            print('That column is full. Try again.')
            return manualPlay(board, piece)

    except ValueError:
        print('Invalid input. Try again.')
        return manualPlay(board, piece)

# Random Play
def randomPlay(board, piece):
    col = random.randrange(0,board.cols)
    while(not board.addToCol(col, piece)):
        return randomPlay(board, piece)
    return 0

# Left to Right Play
def leftToRightPlay(board, piece):
    for j in range(board.cols):
        if board.addToCol(j, piece):
            return True
        else:
            continue
    return False

##################
## Player Class ##
##################
class Player:
    def __init__(self, piece, style):
        self.piece = piece
        self.style = style

    def play(self, board):
        styles = {
            'manual' : manualPlay,
            'random' : randomPlay,
            'leftToRight' : leftToRightPlay
        }
        return styles[self.style](board, self.piece)
######################
## End Player Class ##
######################

###############
## Main Loop ##
###############
def main(args):
    b = Board(args.rows, args.cols)
    b.display()

    p1 = Player('X', 'manual')
    p2 = Player('O', args.style)
    players = [p1,p2]

    while(True):
        for p in players:
            p.play(b)
            b.display()

            # Was there a winner?
            if b.isWinner(p.piece, args.connect):
                print(p.piece + ' wins!')
                return 0 # Success

            # Are there any moves left?
            if b.isFull():
                print('The board is full, there is no winner.')
                return 1 # Failure
##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='Connect N. Connect the pieces without pieces')

# Determine the style of play for player two
parser.add_argument('--style', dest='style', type=str, default='random',
                    help='The style of player for player 2')

# Determine the size of pieces in a row that determine a win
parser.add_argument('--connect', dest='connect', type=int, default='4',
                    help='The number of pieces in a row for a win')

# Determine the size of the board
parser.add_argument('--rows', dest='rows', type=int, default='6',
                    help='The number of rows in the board')
parser.add_argument('--cols', dest='cols', type=int, default='7',
                    help='The number of columns in the board')

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    main(args)
