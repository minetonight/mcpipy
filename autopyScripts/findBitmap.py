import autopy

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

res = findBitmapOnScreen('gitHub_signup.png') 
print "result is %s!" % str(res)
