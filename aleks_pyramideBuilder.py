import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import random
import server

"""user variables"""
# base center coordinates
x0 = 321
y0 = 119
z0 = 86

sideX = 20 # base dimentions
sideZ = 25
slopeXRatio = 1 # the vertical size of pyramide steps
slopeZRatio = 2
offsetX = 1 # the horisontal size of the pyramide steps
offsetZ = 2
#material_id = block.AIR.id # to clean what you did :D
material_id = block.SANDSTONE.id

# your world spown location
spawnX = 200
spawnY = 65
spawnZ = 200

"""eof user variables"""

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

while (widthX >= sideX/2 or slopeXRatio < 1) and (widthZ >= sideZ/2 or slopeZRatio < 1):
  print "widthX=%s, widthZ=%s" % (widthX, widthZ)
  #put layer of the material
  mc.setBlocks(x1+dx, y1+level, z1+dz, x1+widthX, y1+level, z1+widthZ, material_id)
  print "level %s" % level
  
  level += 1
  
  if slopeXRatio > 0 and level % slopeXRatio == 0:
    dx += offsetX
    widthX -= offsetX
  if slopeZRatio > 0 and level % slopeZRatio == 0:
    dz += offsetZ
    widthZ -= offsetZ
  
  
#eof while




