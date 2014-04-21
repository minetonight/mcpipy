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



if __name__ == "__main__":
	
	"""user variables"""
	# your world spawn location
	spawnX = 200
	spawnY = 63
	spawnZ = 200


	# temple center coordinates
	x0 = 321
	z0 = 86
	y0 = 119
	
	"""Maze settings """
	#floor_material_id = block.AIR.id # to clean what you did :D
	#wall_material_id = floor_material_id
	maze_floor_material_id = block.REDSTONE_ORE.id
	maze_wall_material_up = (block.SANDSTONE_CHISELED.id, block.SANDSTONE_CHISELED.data)
	maze_wall_material_low = block.SANDSTONE.id

	# Define the X and Y size of the self.maze including the outer walls.
	# These values aren't checked but must be positive odd integers above 3.
	mazeXSize = 27
	mazeZSize = 21

	"""eof user variables"""

	maze_pos = Vec3()
	maze_pos.x = x0 - spawnX - mazeXSize/2
	maze_pos.z = z0 - spawnZ - mazeZSize/2
	maze_pos.y = y0 - spawnY
	
	mazeBuilder = MazeBuilder(maze_pos, mazeXSize, mazeZSize, maze_floor_material_id, maze_wall_material_low, maze_wall_material_up)
	maze_Conn = MazeConnector()
	maze_loot = MazeChestGenerator(Vec3(spawnX, spawnY, spawnZ))
	
	mazeBuilder.createMaze()
	maze_loot.setRange(mazeBuilder.ppos, mazeBuilder.ppos+Vec3(mazeBuilder.mazeXSize, 0, mazeBuilder.mazeZSize))
	maze_loot.placeChests(mazeBuilder.mazeXSize/7)

	mazeBuilder.ppos.y += 3 # go to next floor
	mazeBuilder.ppos.x += 2 
	mazeBuilder.ppos.z += 2 	
	mazeBuilder.mazeXSize -= 4
	mazeBuilder.mazeZSize -= 4

	mazeBuilder.createMaze()
	maze_Conn.setRange(mazeBuilder.ppos, mazeBuilder.ppos+Vec3(mazeBuilder.mazeXSize, 0, mazeBuilder.mazeZSize))
	maze_Conn.connect(mazeBuilder.mazeXSize/1)
	maze_loot.setRange(mazeBuilder.ppos, mazeBuilder.ppos+Vec3(mazeBuilder.mazeXSize, 0, mazeBuilder.mazeZSize))
	maze_loot.placeChests(mazeBuilder.mazeXSize/7)
	
#eof main
