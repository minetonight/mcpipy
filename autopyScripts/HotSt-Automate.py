# coding=UTF-8
import autopy
from autopy import key
from autopy import mouse
import time
import sys
from random import randint

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# levels = ["TotSQ":{230,155}, "GT":{230,155}, "CH":{230,155}, "DS":{230,155}, "HM":{250,235}, "BB":{230,155}, "DT":{230,155?}]

width, height = autopy.screen.get_size()


print ("")
print ("You have 10 seconds")
time.sleep(10)

def moveHero():
    print ("moveHero")
    
    ###move back and forth
    # x = width/2
    # y = height/2
    # mouse.smooth_move(x-randint(100,300)*direction, y-randint(0,100)) #ahead
    # mouse.click(mouse.RIGHT_BUTTON)
    # time.sleep(5)
    # mouse.smooth_move(x+randint(50,100)*direction, y-randint(0,100)) # back
    # mouse.click(mouse.RIGHT_BUTTON)
    
    ###use mini map
    x = width-230 # BB map
    y = height-155 # BB map
    
    for i in range(3):
        x = x - randint(-50,50) # ahead
        y = y - randint(-50,50) 
        #y = y - randint(0,1)*(235-155) # haunted mines offset
        
        mouse.smooth_move(x, y) #minimap
        key.tap('a')
        
        #TODO ALT callout
        
        mouse.click()
        time.sleep(16)
#eof moveHero

def chooseTalent():
    print ("chooseTalent")
    for i in range(3):
        key.tap(str(randint(1,5)), key.MOD_CONTROL)
#eof chooseTalent

def useTalents():
    print ("useTalents")
    x = width/2
    y = height/2
    for char in ['q', 'w', 'e', 'r', 'd', '1', '2', '3', '4', '5']:
        mouse.smooth_move(x-randint(-100,100), y-randint(100,100)) #ahead
        key.tap(char)
        mouse.click()
        time.sleep(0.5)
        key.tap(char)
        mouse.click(mouse.RIGHT_BUTTON)
#eof useTalents    

def useHeartStone():
    key.tap('b')
    time.sleep(7)
# eof useHeartStone

def startMatch():
    print ("startMatch")
    x = width/2
    y = height - 105 # find "Ready" button
    
    mouse.smooth_move(x, y)
    mouse.click()
    time.sleep(0.5)
#eof startMatch

def endMatch():
    print ("startMatch")
    x = 50
    y = height - 100 # find "Leave" button
    
    mouse.smooth_move(x, y)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
#eof endMatch

while True:

    startMatch()
    chooseTalent()
    moveHero()
    useTalents()
    useHeartStone()
    endMatch()
