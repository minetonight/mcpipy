import sys
import math
from random import randint as rand

EMPTY_CELL = 0
WIDTH = 30
HEIGHT = 20

def display (two_d_array):
    print >> sys.stderr, "display"
    
    for x in range(WIDTH):
		for y in range(HEIGHT):
			element = two_d_array[x][y]
			if element == EMPTY_CELL:
				print >> sys.stderr,"*",
			else:
			    print >> sys.stderr, element,
		print >> sys.stderr, '\n'
#eof display

class Controller:
	
    def __init__(self):
        self.field = [EMPTY_CELL] * WIDTH
        for col in range(len(self.field)):
            self.field[col] = [EMPTY_CELL] * HEIGHT
        
	    self.verbose = False
	    self.verbose = True
	#eof __init__
    
    def updatePlayersWalls(self, player, pos):
        self.field[pos[0]] [pos[1]] = player + 1 #non zero elements
        if self.verbose:
            display(self.field)
    #eof updatePlayersWalls
    

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

controller = Controller()
# game loop
while 1:
     # n: total number of players (2 to 4).
     # p: your player number (0 to 3).
    n, p = [int(i) for i in raw_input().split()]
    for i in xrange(n):
         # x0: starting X coordinate of lightcycle (or -1)
         # y0: starting Y coordinate of lightcycle (or -1)
         # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
         # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in raw_input().split()]
        controller.updatePlayersWalls(i, (x1, y1))

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line with UP, DOWN, LEFT or RIGHT
    dir = rand(1,4)
    print >> sys.stderr, "dir = "+str(dir)
    if dir == 1:
        print "LEFT"
    if dir == 2:
        print "RIGHT"
    if dir == 3:
        print "DOWN"
    if dir == 4:
        print "UP"
