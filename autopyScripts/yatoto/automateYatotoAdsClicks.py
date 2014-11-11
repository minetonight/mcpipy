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
        print "There is no %s... what kind of screen is this?!" % str(filename_png)
    
    return pos
#eof findBitmapOnScreen  
  

def _findBitmapsOnScreen(filename_png):
    """Not working as expected"""
    reference = autopy.bitmap.Bitmap.open(filename_png)
    screen = autopy.bitmap.capture_screen()

    coords = screen.find_every_bitmap(reference)
    if coords:
        print "We found some! They are at %s!" % str(coords)
    else:
        print "There is no reference... what kind of screen is this?!"
    
    return coords
#eof findBitmapsOnScreen


def click_ad(pos):
  delta = 100
  mouse.smooth_move(pos[0]+delta, pos[1]+delta)
  mouse.click()
  mouse.smooth_move(pos[0], 0) # move mouse away
  
  #"find the спечели билет button"
  pos = None
  while True:
    time.sleep(1) # wait for the ads page to load 1s
    pos = findBitmapOnScreen('yatoto_specheli.png')
    if pos:
      break
    
  mouse.smooth_move(pos[0]+10, pos[1]+10)
  mouse.click()
  mouse.smooth_move(pos[0], 0) # move mouse away
    
  pos = None
  #"wait 2 seconds and look for вземи билета. if absent repeat"
  while True:
    time.sleep(2) # wait for the ads page to load 6s
    pos = findBitmapOnScreen('yatoto_specheli.png')
    if pos:
      break
    
  mouse.smooth_move(pos[0]+10, pos[1]+10)
  mouse.click()
  mouse.smooth_move(pos[0], 0) # move mouse away
  
  
  #"close the current tab with ctrl+W"
  time.sleep(2)
  key.tap('w', key.MOD_CONTROL)

  time.sleep(2)
#eof click_ad
  

#"presume the yatoto site is open"
autopy.alert.alert("open www.yatoto.com to start")

first_row_ads_clicked = 0
done = False

#"-main loop-"
while not done:
  
  #find the search area and click a little to the left
  pos = findBitmapOnScreen('yatoto_search.png')
  mouse.smooth_move(pos[0]-350, pos[1]+0)
  mouse.click()
  
  time.sleep(12) # wait for the ads page to load 30s
  
  #scroll down one row
  tap_count_to_scroll_one_row = 10
  for i in range(tap_count_to_scroll_one_row):
    key.tap(key.K_DOWN)
    time.sleep(0.1)
  
  coords = findBitmapOnScreen('yatoto_done.png')
  if coords != None:
    done = True
  
  coords = findBitmapOnScreen('yatoto_ad_corner.png')
  if coords != None:
    click_ad(coords)

#"-end of main loop-"

#close yatoto
key.tap('w', key.MOD_CONTROL)
print ("All ads clicked. Exiting")