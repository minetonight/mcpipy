# coding=UTF-8
import autopy
from autopy import key
from autopy import mouse
import time

def findBitmapOnScreen(filename_png):
    """Look for the reference. Tell me if you found it."""
    reference = autopy.bitmap.Bitmap.open(filename_png)
    screen = autopy.bitmap.capture_screen()

    pos = screen.find_bitmap(reference)
    if pos:
        print "We found him! He's at %s!" % str(pos)
    else:
        print "There is no reference... what kind of screen is this?!"
    
    return pos


def attack():
	#swing
	mouse.click()
	time.sleep(0.3)

#eof attack


def eat():
  consume(9) # food is at 9
#eof eat


def consume(index = 9):
	key.tap( str(index) )
	mouse.toggle(True, mouse.RIGHT_BUTTON) # press down
	time.sleep(4)
	mouse.toggle(False, mouse.RIGHT_BUTTON) # release
	key.tap('1') # sword is at 1
#eof consume


drink_counter = 0

def drink(water_supplies):
  """Returns False if we are out of water"""
  
  find_water_bottle()
  
  assert water_supplies <= 7
  global drink_counter
  first_water_index = 2

  consume(drink_counter + first_water_index)
  drink_counter += 1
  
  return drink_counter < water_supplies
#eof drink


def find_water_bottle():
  key.tap('i') # open inventory
  time.sleep(1)
  
  pos = findBitmapOnScreen('MC_fullBottle.png')
  mouse.smooth_move(pos[0], pos[1]) # point the bottle
  time.sleep(3)
  
  key.tap('i') # close inventory
  time.sleep(1)
#eof find_water_bottle



#"presume minecraft is open"
autopy.alert.alert("Aim at your XP farm and start")

#"-main loop-"
start = time.time()
stop_flag = True
while stop_flag:
  
  for i in range(40):
    attack()
  
  eat()
  
  end = time.time()
  if (end - start) > 6*60: # every 6 min we lose 1 point thirst
    stop_flag = drink(3)
    start = end
  
#"-end of main loop-"

print ("You are out of water, enough farming!")
key.tap(key.K_F4, key.MOD_ALT) # close the game
