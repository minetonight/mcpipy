import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import time
from mcpi.vec3 import Vec3


class AnvilSwitcher:
    
  def __init__(self, vec3_centrePos, vec3_spawn):
    
    offset = 7
    depth = 8 * 8
    centre = vec3_centrePos - vec3_spawn
    
    self.minX = centre.x - offset
    self.maxX = centre.x + offset
    self.minY = centre.y - depth
    self.maxY = centre.y + 3
    self.minZ = centre.z - offset
    self.maxZ = centre.z + offset
    
  #eof init
  
  
  def switch(self):
    
    # Connect to Minecraft.
    try:
      self.mc = minecraft.Minecraft.create(server.address)
    except:
      print "Cannot connect to Minecraft."
      sys.exit(0)
  
    
    IRON_BLOCK = block.IRON_BLOCK.id
    ANVIL = block.ANVIL.id
    counter = 0
    
    for y in reversed(range(self.minY, self.maxY)):
      time.sleep(2)
      for z in range(self.minZ, self.maxZ):
        time.sleep(1)
        for x in range(self.minX, self.maxX):
          time.sleep(0.3)
          print("Checked x(%s of %s) y(%s of %s) z(%s of %s)" % (x, self.maxX, y, self.maxY, z, self.maxZ) )
          if self.mc.getBlock(x, y, z) == IRON_BLOCK:
            self.mc.setBlock(x, y, z, ANVIL)
            counter += 1
            print("   Oh, I found one! %s so far!" % (counter))
    
    
  #eof switch

#eof AnvilSwitcher



if __name__ == "__main__":
  
  """user variables"""
  # your world spawn location
  spawnX = 200
  spawnY = 63
  spawnZ = 200
  spawn = Vec3(spawnX, spawnY, spawnZ)
  
  # catacombs centre coordinates
  centres = [
             Vec3(47, 63, 756),
             Vec3(2210, 64, 1601),
             Vec3(-3688, 106, -1136),
             Vec3(12864, 71, -7620),
             Vec3(27352, 75, -3078),
             Vec3(697, 64, 9417),
             Vec3(20, 60, 9244),
             ]
  
  for centre in centres:
    try:
        
      print ("Working on %s" % (centre) )
      
      switcher = AnvilSwitcher(centre, spawn)
      switcher.switch()
      
      print ("Moving to next catacomb!")
      time.sleep(5)
    except Exception, e:
      print ("Something happened: %s" % (e.message))
    
#eof main
 
