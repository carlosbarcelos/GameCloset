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
    n[orth], s[outh], e[ast], w[est] - Determine the direction in which to travel
    use [item] - Performs an action with a given item
    take [item] - Take an item found in the world
    map - Display the map with a legend

  MAP
    TODO

  TODO
    Might want to seperate class files into seperate files once they get too large.
    Should the screens know their connections? Or is that a job for the world?
'''

import argparse # Command line arguments

##################
## Parser Class ##
##################
class Parser():
    # Get the action word and additional options
    def stripInputOptions():
        return []

    # Work on input and additional options
    def workInputOptions():
        return False
######################
## End Parser Class ##
######################

##################
## Screen Class ##
##################
class Screen():
    def __init__(self, title, items, objects):
        self.title = title
        self.items = items
        self.objects = objects
##################
## Screen Class ##
##################

###############
## Main Loop ##
###############
def main(args):
    print('In development')
    return 1 # Failure
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
