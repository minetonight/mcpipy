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


#"presume the yatoto site is open"
autopy.alert.alert("open www.yatoto.com to start")

#"click the black реклами button"

pos = findBitmapOnScreen('yatoto_reklami_black.png')
mouse.smooth_move(pos[0]+10, pos[1]+10)
mouse.click()
#"-main loop-"
while True:
	
	time.sleep(12) # wait for the ads page to load 30s
	
	#"move reatively below on an ad"
	pos = mouse.get_pos()
	delta = 100 + 1*145 # one sponsored ad
	mouse.smooth_move(pos[0], pos[1]+delta)
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
		pos = findBitmapOnScreen('yatoto_vzemi.png')
		if pos:
			break
		
	mouse.smooth_move(pos[0]+10, pos[1]+10)
	mouse.click()
	mouse.smooth_move(pos[0], 0) # move mouse away
	
	
	#"close the current tab with ctrl+W"
	time.sleep(2)
	key.tap('w', key.MOD_CONTROL)

	time.sleep(2)
	#"click the orange реклами button so that the ads reload"
	pos = findBitmapOnScreen('yatoto_reklami_orange.png')
	mouse.smooth_move(pos[0]+10, pos[1]+10)
	mouse.click()

#"-end of main loop-"
