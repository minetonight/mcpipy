import mcpi.minecraft as minecraft
import mcpi.block as block
import sys, random
from random import randint as rand
import server
from mcpi.vec3 import Vec3 
from math import sqrt
from aleks_mazeBuilder import MazeBuilder
from aleks_mazeConnector import MazeConnector
from aleks_mazeChestGenerator import MazeChestGenerator
from aleks_pyramideBuilder import PyramideBuilder

class TempleBuilder:
  
  def __init__(self, mazeLevels, vec3_centrePos, vec3_spawn):
    self.mazeLevels = mazeLevels
    self.templeCentre = vec3_centrePos
    self.spawn = vec3_spawn
    
    self.topMazeWidth = 5
  #eof init
  
  def build(self):
    self._buildPyramide()
    self._buildMazes()
  #eof build
  
  def _buildPyramide(self):
    # base width depending on the levels
    # each level adds 2*mazeHeight=6 more blocks to the top maze with
    self.baseWidth = (self.mazeLevels * (3 * 2)) + self.topMazeWidth
	  
    sideX = self.baseWidth # base dimentions
    sideZ = self.baseWidth
    slopeXRatio = 1 # the vertical size of pyramide steps
    slopeZRatio = 1
    offsetX = 1 # the horisontal size of the pyramide steps
    offsetZ = 1
    #material_id = block.AIR.id 				# to clean what you did :D
    material_id = block.GOLD_BLOCK.id
    
    #calc starting corner point
    self.vec3_corner = self.templeCentre - self.spawn - Vec3( sideX/2, 0, sideZ/2)
    #x1 = x0 - sideX/2 - spawnX
    #y1 = y0 - spawnY
    #z1 = z0 - sideZ/2 - spawnZ
    
    builder = PyramideBuilder(self.vec3_corner, sideX, sideZ, slopeXRatio, slopeZRatio, offsetX, offsetZ, material_id)
    builder.createPyramide()
    
  #eof _buildPyramide
  
  
  def _buildMazes(self):
    	"""Maze settings """
    maze_floor_material_id = block.REDSTONE_ORE.id
    maze_wall_material_up = (block.SANDSTONE_CHISELED.id, block.SANDSTONE_CHISELED.data)
    maze_wall_material_low = block.SANDSTONE.id
    
    delta = Vec3(3,3,3)
    mazeXSize = self.baseWidth - 6
    mazeZSize = self.baseWidth - 6
    maze_pos = self.vec3_corner - Vec3(0, 3, 0)  # 3 below, for easier iteration later
    maze_pos += delta
    currLevel = 1
    """eof user variables"""
    
    mazeBuilder = MazeBuilder(maze_pos, mazeXSize, mazeZSize, maze_floor_material_id, maze_wall_material_low, maze_wall_material_up)
    maze_Conn = MazeConnector()
    maze_loot = MazeChestGenerator(self.spawn)
    
    #create lowest level then loop the rest
    mazeBuilder.createMaze()
    maze_loot.setRange(maze_pos, maze_pos + Vec3(mazeXSize, 0, mazeZSize))
    numChests = mazeXSize/5
    itemsPerChest = 27 / numChests
    maze_loot.placeChests(numChests, itemsPerChest)
    
    
    
    
    while mazeXSize > self.topMazeWidth:
      currLevel += 1
      mazeXSize -= 6
      mazeZSide -= 6
      maze_pos += delta
      
      mazeBuilder.ppos = maze_pos
      mazeBuilder.mazeXSize = mazeBuilder.mazeZSize = mazeXSize
      mazeBuilder.createMaze()
      
      maze_end = maze_pos + Vec3(mazeXSize, 0, mazeZSize)
      numChests = mazeXSize/5                             #TODO
      itemsPerChest = 27 / numChests                       #TODO
      maze_loot.setRange(maze_pos, maze_end)
      maze_loot.placeChests(numChests, itemsPerChest)
      
      maze_Conn.setRange(maze_pos, maze_end)
      maze_Conn.connect(mazeXSize/1)                       #TODO
	
      
    #eof while > topMazeWidth
    
  #eof _buildMazes
  
#eof TempleBuilder


if __name__ == "__main__":
  
  """user variables"""
  # your world spawn location
  spawnX = 200
  spawnY = 63
  spawnZ = 200
  spawn = Vec3(spawnX, spawnY, spawnZ)
  
  # temple center coordinates
  x0 = 321
  z0 = 86
  y0 = 119
  centre = Vec3(x0, y0, z0)
  
  levels = 18 # limited by the 490 loot items
  	
  temple = TempleBuilder(levels, centre, spawn)
  temple.build()
#eof main
