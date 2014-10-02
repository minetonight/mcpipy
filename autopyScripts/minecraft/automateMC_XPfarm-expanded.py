# coding=UTF-8
import autopy
from autopy import key
from autopy import mouse
import time

directions=[]
drink_counter = 0

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
	##pos = mouse.get_pos()
	##mouse.smooth_move(pos[0], pos[1]+delta)
	##mouse.smooth_move(pos[0]+10, pos[1]+10)

#eof attack


def eat():
  consume(9) # food is at 9
#eof eat


def consume(index = 9):
	print("in consume")
	key.tap( str(index) )	
	time.sleep(0.3)
	mouse.toggle(True, mouse.RIGHT_BUTTON)
	time.sleep(4)
	mouse.toggle(False, mouse.RIGHT_BUTTON)
	time.sleep(0.3)
	key.tap('1') # sword is at 1
	print("end consume")
#eof consume


def drink(water_supplies):
  """Returns False if we are out of water"""
  assert water_supplies <= 8
  global drink_counter
  first_water_index = 1

  consume(drink_counter + first_water_index)
  drink_counter += 1
  
  return drink_counter < water_supplies
#eof drink


def refillHotbar(row):
  
  grid_step = 36
  
  #open inventory
  key.tap('i')
  time.sleep(1)
  
  #find the first pos of the hot bar
  pos = findBitmapOnScreen('MC_cornerBottle.png') 
  cornerpos = (pos[0] + grid_step/2, pos[1] + grid_step/2)
  mouse.smooth_move(cornerpos[0], cornerpos[1])
  
  for col in range(9):
    mouse.smooth_move(cornerpos[0] + (col*grid_step), 
                      cornerpos[1] - (row * grid_step))
    time.sleep(0.3)
    key.tap(str(col + 1))
    time.sleep(0.3)
    print(str(col + 1))

  #close inventory
  global drink_counter
  
  #reset the drink counter
  drink_counter = 0
  key.tap('i')
  time.sleep(1)

#"presume minecraft is open"
autopy.alert.alert("Aim at your XP farm and start")

#"-main loop-"
for count in range(1, 3+1):

  start = time.time()
  hotbar_empty = False
  while not hotbar_empty:
    
    for i in range(600): # 600
      attack()
    
    eat()
    
    end = time.time()
    if (end - start) > 2*6*60: # 2*6*60 every 6 min we lose 1 point thirst
      has_more_water = drink(8)
      hotbar_empty = not has_more_water
      start = end
  #eof while not hotbar_empty
  
  try:
    refillHotbar(count)
  except:
    print ("Something unexpected happened: %s" % sys.exc_info()[0])

#"-end of main loop-"
else: 
  print ("You are out of water, enough farming!")

key.tap(key.K_F4, key.MOD_ALT)
