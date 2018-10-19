# The game of war. By CJ Barcelos.
# V1: 5/19/2015
# V2: 10/19/2018

from random import randint
import time

# Initalization
P1 = []
P2 = []
pot = []
pos = 0
rnd = 0

# Define deck constraints
A = 14 # Add in Aces low feature using raw input
suit = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, A]
deck = suit+suit+suit+suit

# Deal function takes deck and splits evenly and randomly.
def deal():
    global P1
    global P2
    global deck
    for n in range (0, 52):            # Why is this number 52?
        ran = randint(0,len(deck) - 1) # Obtain random position in deck
        randeck = deck[ran]            # Record randomly selected card
        if n%2 == 0:                   # Add card to either P1 or P2
             P1 += [randeck]
        else: P2 += [randeck]
        deck.remove(randeck)             # Remove card from deck
        #print len(deck)                # How many cards left in deck?
        #print P1                       # What is P1's hand now
        #print P2                       # What is P2's hand now

# Play function considers the first cards in each player's deck
# and plays the game until one player runs out of cards.
def play():
    global pot
    global P1
    global P2
    global pos
    global rnd
    print("Player 1's Starting Hand:")
    print(P1)
    print("Player 2's Starting Hand:")
    print(P2)
    while len(P1) != 0 and len(P2) != 0:
        pot = [P1[0]] + [P2[0]]
        P1.remove(P1[0])
        P2.remove(P2[0])
        rnd += 1
        print("Round" + " " + str(rnd))
        print(pot)
        if pot[0] > pot[1]:                 # P1 Wins round
            P1 += pot      # ADD feature to alterate how cards are placed in hand to avoid endless games
            pot = []
            print("P1 Wins Round")
            print("P1 Hand: " + str(len(P1)))
            print("P2 Hand: " + str(len(P2)))
        elif pot[0] < pot[1]:               # P2 Wins round
            P2 += pot
            pot = []
            print("P2 Wins Round")
            print("P1 Hand: " + str(len(P1)))
            print("P2 Hand: " + str(len(P2)))
        else: tie()                         # War tie breaker
        print("//////////////////////////////")


def tie():      # WORK ON THIS!!! Make so running out of cards dosen't end game.
    global pot
    global P1
    global P2
    global pos
    if len(P1) < 4:
        print("Player 1 Ran Out of Cards.")
    elif len(P2) < 4:
        print("Player 2 Ran Out of Cards.")
    else:
        if len(P1) == 0:          # Is this part necessary??????
            print ("P2 Wins! Congratulations P2!")
        elif len(P2) == 0:
            print("P1 Wins! Congratulations P1!")
        else:
            if len(pot) == 2:
                pos += 5
            else:
                pos += 8
            pot = pot + P1[0:4] + P2[0:4]
            del P1[0:4]
            del P2[0:4]
            if pot[pos] > pot[pos + 4]:
                P1 += pot
                pot = []
                pos = 0
                print("P1 Wins Round")
                print("P1 Hand: " + str(len(P1)))
                print("P2 Hand: " + str(len(P2)))
            elif pot[pos] < pot[pos + 4]:
                P2 += pot
                pot = []
                pos = 0
                print("P2 Wins Round")
                print("P1 Hand: " + str(len(P1)))
                print("P2 Hand: " + str(len(P2)))
            else: tie()

# Result function outputs a winning mesage based on which player runs of cards.
def report():
    if len(P1) == 0:
        print("P2 Wins! Congratulations P2!")
    elif len(P2) == 0:
        print("P1 Wins! Congratulations P1!")
    else: print("Something Went Wrong.")

# Reset function sets variables to initial state as to play again.
def reset():
    global P1
    global P2
    global deck
    global rnd
    P1 = []
    P2 = []
    deck = suit + suit + suit + suit
    rnd = 0

# War function plays all stages of game in order.
def war():
    start_time = time.time()
    deal()
    play()
    report()
    reset()
    print("This game took %s seconds to play" % (time.time() - start_time))

# Run Main
if __name__ == '__main__':
    war()
