#!/usr/bin/env python

# Quick rough & ready maze generator for Minecraft Pi edition.
# Dave Finch 2013

# mcpipy.com retrieved from URL below, written by davef21370
# https://github.com/brooksc/mcpipy/blob/master/davef21370_maze.py

import mcpi.minecraft as minecraft
import mcpi.block as block
import sys, random
from random import randint as rand
import server
from mcpi.vec3 import Vec3



# Create a function for picking a random direction.
def randDir():
    r = rand(0, 3)
    if r == 0: rv = (0, -1) # Up.
    if r == 1: rv = (0, 1) # Down.
    if r == 2: rv = (-1, 0) # Left.
    if r == 3: rv = (1, 0) # Right.
    return rv
#eof randDir


class MazeBuilder:
	
	def __init__(self, mazeCorner_vec3, mazeXSize, mazeZSize, floorMaterial, wallMaterial_low, wallMaterial_up):
		self.ppos = mazeCorner_vec3
		self.mazeXSize = mazeXSize
		self.mazeZSize = mazeZSize
		self.floor_material_id = floorMaterial
		self.wall_material_low = wallMaterial_low
		self.wall_material_up = wallMaterial_up
		
		# Set the maximum length of a wall.
		self.maxWallLen = 1
	#eof __init__

	
	# Create a function to initialize the maze.
	# w and h are the width and height respectively.
	def initMaze(self, w, h):
			# Create a 2 dimensional array.
			self.maze = [[0]*h for x in range(w)]

			# Create four walls around the maze.
			# 1=wall, 0=walkway.
			for x in range(0, w):
					self.maze[x][0] = self.maze[x][h-1] = 1
					self.makeWall(self.ppos.x+x, self.ppos.z+0)
					self.makeWall(self.ppos.x+x, self.ppos.z+h-1)
			for y in range(0, self.mazeZSize):
					self.maze[0][y] = self.maze[w-1][y] = 1
					self.makeWall(self.ppos.x, self.ppos.z+y)
					self.makeWall(self.ppos.x+w-1, self.ppos.z+y)

			# Make every other cell a starting point.
			# 2=starting point.
			# Also create a list of these points to speed up the main loop.
			self.spl = []
			for y in range(2, h-2, 2):
					for x in range(2, w-2, 2):
							self.maze[x][y] = 2
							self.spl.append((x, y))
			# Shuffle the list of points and we can choose a random point by
			# simply "popping" it off the list.
			random.shuffle(self.spl)
	#eof initMaze


	def makeWall(self, x, z):
			self.mc.setBlock(x, self.ppos.y, z, self.floor_material_id)
			self.mc.setBlock(x, self.ppos.y+1, z, self.wall_material_low)
			self.mc.setBlock(x, self.ppos.y+2, z, self.wall_material_up)
	#eof makeWall


	def createMaze(self): 
		
		# Connect to Minecraft.
		try:
				self.mc = minecraft.Minecraft.create(server.address)
		except:
				print "Cannot connect to Minecraft."
				sys.exit(0)
		
		
		# Clear an area for the maze.
		for x in range(0, self.mazeXSize-1):
				for z in range(self.mazeZSize-1):
						self.mc.setBlock(self.ppos.x+x, self.ppos.y, self.ppos.z+z, self.floor_material_id)
						for y in range(1, 3):
								self.mc.setBlock(self.ppos.x+x, self.ppos.y+y, self.ppos.z+z, block.AIR)

		# Create an empty maze.
		self.initMaze(self.mazeXSize, self.mazeZSize)

		# Loop until we have no more starting points (2's in the empty maze)
		while filter(lambda x: 2 in x, self.maze):
				# Get the X and Y values of the first point in our randomized list.
				rx = self.spl[0][0]
				ry = self.spl[0][1]
				# Pop the first entry in the list, this deletes it and the rest move down.
				self.spl.pop(0)
				# Check to see if our chosen point is still a valid starting point.
				ud = False
				if self.maze[rx][ry] == 2:
						ud = True
						# Pick a random wall length up to the maximum.
						rc = rand(0, self.maxWallLen)
						# Pick a random direction.
						rd = randDir()
						fc = rd
						loop = True
						while loop:
								# Look in each direction, if the current wall being built is stuck inside itself start again.
								if self.maze[rx][ry-2] == 3 and self.maze[rx][ry+2] == 3 and self.maze[rx-2][ry] == 3 and self.maze[rx+2][ry] == 3:
										#
										# Code to clear maze area required
										#
										self.initMaze(self.mazeXSize, self.mazeZSize)
										break
								# Look ahead to see if we're okay to go in this direction.....
								cx = rx + (rd[0]*2)
								cy = ry + (rd[1]*2)
								nc = self.maze[cx][cy]
								if nc != 3:
										for i in range(0, 2):
												self.maze[rx][ry] = 3
												self.makeWall(self.ppos.x+rx, self.ppos.z+ry)
												rx += rd[0]
												ry += rd[1]
								# .....if not choose another direction.
								else: rd = randDir()
								# If we hit an existing wall break out of the loop.
								if nc == 1: loop = False
								# Update our wall length counter. When this hits zero pick another direction.
								# This also makes sure the new direction isn't the same as the current one.
								rc -= 1
								if rc <= 0:
										rc = rand(0, self.maxWallLen)
										dd = rd
										de = (fc[0]*-1, fc[1]*-1)
										while dd == rd or rd == de:
												rd = randDir()
				# The latest wall has been built so change all 3's (new wall) to 1's (existing wall)
				if ud:
						for x in range(0, self.mazeXSize):
								for y in range(0, self.mazeZSize):
										if self.maze[x][y] == 3: self.maze[x][y] = 1
	#eof createMaze
#eof MazeBuilder


if __name__ == "__main__":
	
	"""user variables"""
	# your world spawn location
	spawnX = 200
	spawnY = 65
	spawnZ = 200


	# base center coordinates
	x0 = 321
	z0 = 86
	y0 = 119

	#floor_material_id = block.AIR.id # to clean what you did :D
	#wall_material_id = floor_material_id
	floor_material_id = block.REDSTONE_ORE.id
	wall_material_up = (block.SANDSTONE_CHISELED.id, block.SANDSTONE_CHISELED.data)
	wall_material_low = block.SANDSTONE.id

	# Define the X and Y size of the self.maze including the outer walls.
	# These values aren't checked but must be positive odd integers above 3.
	mazeXSize = 17
	mazeZSize = 21

	"""eof user variables"""

	pos = Vec3()
	pos.x = x0 - spawnX - mazeXSize/2
	pos.z = z0 - spawnZ - mazeZSize/2
	pos.y = y0 - spawnY
	
	mazeBuilder = MazeBuilder(pos, mazeXSize, mazeZSize, floor_material_id, wall_material_low, wall_material_up)
	mazeBuilder.createMaze()
#eof main
