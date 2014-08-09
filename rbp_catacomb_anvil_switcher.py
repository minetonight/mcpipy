import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import time
from mcpi.vec3 import Vec3


class AnvilSwitcher:
    
  def __init__(self, vec3_centrePos, vec3_spawn):
    
    offset = 200
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
    
    if not self.mc:
      # Connect to Minecraft.
      try:
          self.mc = minecraft.Minecraft.create(server.address)
      except:
          print "Cannot connect to Minecraft."
          sys.exit(0)
    
    
    IRON_BLOCK = block.IRON_BLOCK.id
    ANVIL = block.ANVIL.id
    counter = 0
    
    for y in range(self.minY, self.maxY):
      for z in range(self.minZ, self.maxZ):
        for x in range(self.minX, self.maxX):
          if self.mc.getBlock(x, y, z) == IRON_BLOCK:
            self.mc.setBlock(x, y, z, ANVIL)
            counter += 1
            print("   Oh, I found one! %s so far!" % (counter))
        time.sleep(1)
        print("Checked x(%s of %s) y(%s of %s) z(%s of %s)" % (x, maxX, y, maxY, z, maxZ) )
    
    
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
  centres = [Vec3(55, 63, 758),
             Vec3(2214, 64, 1600),
             Vec3(-3686, 106, -1139),
             Vec3(12859, 71, -7621),
             Vec3(27344, 75, -3080),
             Vec3(700, 64, 9418),
             Vec3(0, 57, 9250)]
  
  for centre in centres:
    print ("Working on %s" % (centre) )
    
    switcher = AnvilSwitcher(centre, spawn)
    switcher.switch()
    
    print ("Moving to next catacomb!")
    time.sleep(5)
    
#eof main
 
