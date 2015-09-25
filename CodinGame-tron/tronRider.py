import sys
import math
from random import randint as rand
from collections import OrderedDict

EMPTY_CELL = 0
WIDTH = 30
HEIGHT = 20


def debug(str):
    print >> sys.stderr, str
#eof debug


def display (two_d_array):
    #""" To debug: print >> sys.stderr, 'Debug messages...' """
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
        
        self.x = -1
        self.y = -1
        
        self.hasStrategy = False
        self.strategyDirections = ["UP", "LEFT", "DOWN", "RIGHT"] 
        self.mustTurn = True
        self.direction = ""
        
        self.deathUpdated = [False, False, False, False]
        
        self.verbose = True
        self.verbose = False
	#eof __init__
    
    
    def setPlayerId(self, playerId):
        self.playerId = playerId
    #eof setPlayerId
    
    
    def updatePlayersWalls(self, playerId, pos):
        
        #TODO remove dead player walls
        if pos[0] == -1 and not self.deathUpdated[playerId]:
            self.deletePlayerWalls(playerId)
            #debug ("player %s died"%(playerId))
        
        if pos[0] != -1:
            self.field[pos[0]] [pos[1]] = playerId + 1 #non zero elements
        
        if playerId == self.playerId:
            self.x = pos[0]
            self.y = pos[1]
        
        if self.verbose:
            display(self.field)
    #eof updatePlayersWalls
    
    
    def deletePlayerWalls(self, playerId):
        
        for x in range(WIDTH):
            for y in range(HEIGHT):
                element = self.field[x][y]
                if element == playerId + 1:
                    self.field[x][y] = EMPTY_CELL
        
        if self.verbose:
            display(self.field)
        #display(self.field)
        
        self.deathUpdated[playerId] = True
    #eof deletePlayerWalls    
    

    def chooseStrategy(self):
        
        if self.x == -1:
            return
        
        dirDict = {}
        #TODO find closest walls http://stackoverflow.com/a/15179418
        dirDict["LEFT"] = self.x
        dirDict["RIGHT"] = (WIDTH - 1) - self.x
        dirDict["UP"] = self.y
        dirDict["DOWN"] = (HEIGHT - 1) - self.y
        
        dirDict = OrderedDict(sorted(dirDict.items(), key=lambda t: t[1]))
        #debug(str(dirDict))
        #debug(str(dirDict.keys()))
        
        #self.strategyDirections = ["LEFT", "RIGHT", "UP", "DOWN"] 
        self.strategyDirections = dirDict.keys()
        self.direction = self.strategyDirections[0]
        
        self.hasStrategy = True
        
    #eof chooseStrategy 
    
    
    def chooseDirection(self):
        #""" A single line with UP, DOWN, LEFT or RIGHT """
        
        if not self.hasStrategy:
            self.chooseStrategy()
        
        self.mustTurn = not self.isValidMove(self.direction)
        
        dir = -1
        
        while self.mustTurn:
            
            dir = dir + 1
            debug("dir = %s == %s "%(dir, self.strategyDirections[dir]))
            
            self.mustTurn = not self.isValidMove(self.strategyDirections[dir])
            self.direction = self.strategyDirections[dir]
            
        return self.direction
    #eof chooseDirection
    
    
    def isValidMove(self, moveStr):
        pos = self.getNextPos([self.x, self.y], moveStr)
        
        _x = pos[0]
        _y = pos[1]
        
        if ((not (0 <= _x < WIDTH)) or (not (0 <= _y < HEIGHT))):
            
            debug("%s , %s is out of bounds"%(_x, _y))
            return False
        
        if self.field[_x][_y] <= EMPTY_CELL:
            return True
        else:
            debug("val is " + str(self.field[_x][_y]))
            display(self.field)
            return False
    #eof isValidMove


    def getNextPos(self, currPos, moveStr):
        
        if self.verbose:
            debug("currPos = " + str(currPos))
        
        nextPos = [currPos[0], currPos[1]]
        
        if moveStr == "LEFT":
            nextPos[0] = currPos[0] - 1
        if moveStr == "RIGHT":
            nextPos[0] = currPos[0] + 1
        if moveStr == "DOWN":
            nextPos[1] = currPos[1] + 1
        if moveStr == "UP":
            nextPos[1] = currPos[1] - 1
        
        if self.verbose:
            debug("nextPos = " + str(nextPos))
        
        return nextPos
    #eof getNextPos


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

controller = Controller()
# game loop
while 1:
     # n: total number of players (2 to 4).
     # p: your player number (0 to 3).
    n, playerID = [int(i) for i in raw_input().split()]
    controller.setPlayerId(playerID)
    
    for playerIndex in xrange(n):
         # x0: starting X coordinate of lightcycle (or -1)
         # y0: starting Y coordinate of lightcycle (or -1)
         # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
         # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in raw_input().split()]
        controller.updatePlayersWalls(playerIndex, (x1, y1))

    # Write an action using print
    # A single line with UP, DOWN, LEFT or RIGHT
    print controller.chooseDirection()