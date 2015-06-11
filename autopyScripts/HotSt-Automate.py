# coding=UTF-8
import autopy
from autopy import key
from autopy import mouse
import time
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) < 2:
    direction = -1
    print("using default direction left to right")
    print("give a parameter to use right to left")
if len(sys.argv) > 1:
    direction = -1
    print("using right to left direction")
    print("run without parameter to use left to right")
    
width, height = autopy.screen.get_size()


print ("")
print ("You have 10 seconds")
time.sleep(10)

def moveHero():
    print ("moveHero")
    x = width/2
    y = height/2
    mouse.smooth_move(x-100*direction, y)
    mouse.click(mouse.RIGHT_BUTTON)
    time.sleep(5)
    mouse.smooth_move(x+50*direction, y)
    mouse.click(mouse.RIGHT_BUTTON)
#eof moveHero

def chooseTalent():
    print ("chooseTalent")
    key.tap('2', key.MOD_CONTROL)
    key.tap('1', key.MOD_CONTROL)
    key.tap('3', key.MOD_CONTROL)
#eof chooseTalent

def useTalents():
    print ("useTalents")
    x = width/2
    y = height/2
    for char in ['q', 'w', 'e', 'r', 'd', '1', '2', '3', '4', '5']:
        mouse.smooth_move(x-100*direction, y)
        key.tap(char)
        mouse.click()
        time.sleep(1)
        key.tap(char)
        mouse.click(mouse.RIGHT_BUTTON)
    
#eof useTalents    

while True:
    moveHero()
    useTalents()
    chooseTalent()
    
