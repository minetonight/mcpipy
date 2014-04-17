import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import random
import server

x0 = 321
y0 = 119
z0 = 86

sideX = 150
sideZ = 150
slopeXRatio = 1
slopeZRatio = 1
material_id = 1 # TODO sandstone

spawnX = 200
spawnY = 65
spawnZ = 200


#calc starting corner point
x1 = x0 - sideX/2 - spawnX
y1 = y0 - spawnY
z1 = z0 - sideZ/2 - spawnZ

#connect to mc
mc = minecraft.Minecraft.create(server.address)


widthX = sideX
widthZ = sideZ
level = 0
dx = 0
dz = 0

while widthX >= sideX/2 and widthZ >= sideZ/2:
  print "widthX=%s, widthZ=%s" % (widthX, widthZ)
  #put layer of the material
  mc.setBlocks(x1+dx, y1+level, z1+dz, x1+widthX, y1+level, z1+widthZ, material_id)
  print "level %s" % level
  
  level += 1
  
  if level % slopeXRatio == 0:
    dx += 1
    widthX -= 1
  if level % slopeZRatio == 0:
    dz += 1
    widthZ -= 1
  
  
#eof while




