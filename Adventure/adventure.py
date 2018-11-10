'''
@title Text Adventure
@author Carlos Barcelos
@date TODO
'''

'''
Development Notes
  The game WORLD is comprised of a series of SCREENs that are connected
  by DIRECTIONs (north, south, east, or west). In each screen are ITEMs to
  collect and OBJECTs to interact with.

  The PLAYER will travel the world, collecting items in order to [WHAT IS THE OBJECTIVE?].

  ACTIONS
    move dir - Determine the direction in which to travel
    use item - Performs an action with a given item
    take item - Take an item found in the world
    map - Display the map with a legend

  MAP
    TODO

  TODO
    Might want to seperate class files into seperate files once they get too large.
    Should the screens know their connections? Or is that a job for the world?
'''

import argparse # Command line arguments
import sys      # Various system variables
import json     # Handle JSON files

######################
## Player Class ##
######################
class Player():
    def __init__(self):
        self.inventory = []
        self.health = 100
######################
## End Player Class ##
######################

#######################
## Game Engine Class ##
#######################
class GameEngine():
    def __init__(self, map, player):
        self.map = map
        self.player = player
        self.currentRoom = 'Room 1'
        self.verbs = ['move', 'take', 'use', 'map']

    # Promt the user for action
    def prompt(self):
        newInput = input('> ')
        self.parse(newInput)

    # Get the action word and additional options
    def parse(self, inStr):
        returnState = False
        returnDict = {'verb': None, 'noun': None}
        words = inStr.split()

        # Reject empty strings
        if inStr:
            # Accept maximum one word after verb
            if len(words) == 1:
                returnDict['verb'] = words[0]
            elif len(words) == 2:
                returnDict['verb'] = words[0]
                returnDict['noun'] = words[1]
            returnState = self.workInputOptions(returnDict['verb'], returnDict['noun'])
        return returnState

    # Work on input and additional options
    def workInputOptions(self, verb, noun):
        if not verb in self.verbs:
            return False

        switcher = {
            'move': self.move,
            'take': self.take,
            'use': self.use,
            'map': self.displayMap
        }

        func = switcher.get(verb)
        return func(noun)

    # Move a certain direction from the current room
    def move(self, dir):
        if dir is None:
            print('Move requires a direction input: [north, south, east, west].')
            return False

        try:
            nextRoom = self.map['Map'][self.currentRoom]['Connections'][dir]
            self.currentRoom = self.map['Map'][nextRoom]['Title']
            print(self.map['Map'][self.currentRoom]['Description'])
            return True
        except KeyError:
            print(f"Move '{dir}': Invalid direction.")
            print(f"Possible directions from {self.currentRoom}: {self.map['Map'][self.currentRoom]['Connections']}")
            return False

    # Taken a given item and add it to the player inventory
    def take(self, noun):
        if noun is None:
            print('Take requires a noun as input.')
            return False

        returnState = False
        items = self.map['Map'][self.currentRoom]['Items']

        if noun in items:
            self.map['Map'][self.currentRoom]['Items'].remove(noun)
            self.player.inventory.append(noun)
            print(f'Inventory: {self.player.inventory}')
        else:
            print(f'{noun} is not in {self.currentRoom}')

        return returnState

    # Use a given item
    def use(self, noun):
        if noun is None:
            print('Must use a specific item.')
            return False
        returnState = False
        # TODO:
        return returnState

    # Display the map
    def displayMap(self, noun):
        print('TODO: Make a map!')
        return True

    # Determine if the game is over
    def isOver(self):
        # TODO:
        return False
###########################
## End Game Engine Class ##
###########################

###############
## Main Loop ##
###############
def main(args):
    # Initilization
    with open('map.json') as f:
        map = json.load(f)
    player = Player()
    ge = GameEngine(map, player)

    while(not ge.isOver()):
        ge.prompt()

##############
## End Main ##
##############

#########################
## Command-Line Inputs ##
#########################
parser = argparse.ArgumentParser(description='Text Adventure. A text game ... WITH text!')

# TODO Are there any options?

args = parser.parse_args()
##############################
## End Command-Line Inputs ##
#############################

# Run Main
if __name__ == '__main__':
    main(args)
