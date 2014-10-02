# coding=UTF-8
import autopy
from autopy import key
from autopy import mouse
import time

directions=[]
drink_counter = 0

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
	key.tap( str(index) )
	mouse.toggle(True, mouse.RIGHT_BUTTON)
	time.sleep(4)
	mouse.toggle(False, mouse.RIGHT_BUTTON)
	key.tap('1') # sword is at 1
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

#"presume minecraft is open"
autopy.alert.alert("Aim at your XP farm and start")

#"-main loop-"
start = time.time()
stop_flag = True
while stop_flag:
  
  for i in range(600): # 600
    attack()
  
  eat()
  
  end = time.time()
  if (end - start) > 2*6*60: # 2*6*60 every 6 min we lose 1 point thirst
    stop_flag = drink(3)
    start = end
  
#"-end of main loop-"

print ("You are out of water, enough farming!")
key.tap(key.K_F4, key.MOD_ALT)
