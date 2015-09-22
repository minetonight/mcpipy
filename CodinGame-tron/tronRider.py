import sys
import math
from random import randint as rand

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


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
