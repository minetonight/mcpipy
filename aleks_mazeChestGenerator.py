import mcpi.minecraft as minecraft
import mcpi.block as block
import sys, random
from math import *
from random import randint as rand
import server
from mcpi.vec3 import Vec3

class MazeChestGenerator:
	
	def __init__(self, worldSpawn_vec3):
		self.spawnX = worldSpawn_vec3.x
		self.spawnY = worldSpawn_vec3.y
		self.spawnZ = worldSpawn_vec3.z
	#eof init
	
	
	def setRange(self, vec3_from, vec3_to):
		#avoid chests on maze bounding walls
		self.minX = min(vec3_from.x+1, vec3_to.x+1)
		self.minZ = min(vec3_from.z+1, vec3_to.z+1)
		self.maxX = max(vec3_from.x-1, vec3_to.x-1)
		self.maxZ = max(vec3_from.z-1, vec3_to.z-1)
		
		assert vec3_from.y == vec3_to.y, "provide two corner points on the same Y level"
		self.y_level = vec3_to.y + 1 # one above the floor
	#eof setRange
	
	
	def placeChests(self, num_chests):
		
		# Connect to Minecraft.
		try:
			mc = minecraft.Minecraft.create(server.address)
		except:
			print "Cannot connect to Minecraft."
			sys.exit(0)
		
		chests = 0
		
		while chests < num_chests:
			randX = rand(self.minX, self.maxX)
			randZ = rand(self.minZ, self.maxZ)
			corridors = 0
			diagonals = 0
			
			if mc.getBlock(randX, self.y_level, randZ) == block.AIR.id or mc.getBlock(randX, self.y_level, randZ) == block.CHEST_TRAPPED.id:
				continue
			
			"""find the end of a wall, air at exactly three of the sides
			while searching find the direction of the wall"""
			if mc.getBlock(randX, self.y_level, randZ+1) == block.AIR.id:
				corridors += 1	
			else: 
				direction = 0x2 #0x2: Facing north (for ladders and signs, attached to the north side of a block)
			if mc.getBlock(randX-1, self.y_level, randZ) == block.AIR.id:
				corridors += 1	
			else: 
				direction = 0x5 #0x5: Facing east
			if mc.getBlock(randX, self.y_level, randZ-1) == block.AIR.id:
				corridors += 1	
			else: 
				direction = 0x3 #0x3: Facing south
			if mc.getBlock(randX+1, self.y_level, randZ) == block.AIR.id:
				corridors += 1	
			else: 
				direction = 0x4 #0x4: Facing west

			if mc.getBlock(randX+1, self.y_level, randZ+1) == block.AIR.id:
				diagonals += 1
			if mc.getBlock(randX+1, self.y_level, randZ-1) == block.AIR.id:
				diagonals += 1
			if mc.getBlock(randX-1, self.y_level, randZ+1) == block.AIR.id:
				diagonals += 1
			if mc.getBlock(randX-1, self.y_level, randZ-1) == block.AIR.id:
				diagonals += 1


			if corridors == 3 and diagonals == 4:
				mc.setBlock(randX, self.y_level+1, randZ, block.AIR.id)
				mc.setBlock(randX, self.y_level, randZ, block.CHEST_TRAPPED.id, direction) 
				chests += 1
				print ("chest N%s at /tp %s, %s, %s -> %s" % (chests, randX+self.spawnX, self.y_level+self.spawnY+1, randZ+self.spawnZ, self._chestContents()))
		#eof while
		
	#eof placeChests
	
	
	def _chestContents(self):
		"""
		Flesh						50%
		Bones						50%
		Gunpowder				50%
		Iron Ingot			45%
		Gold Ingot			25%
		
		Gold Helmet					25%
		Gold Chestplate 		25%
		Gold Leggings				25%
		Gold Boots					25%
		Chainmail Helmet		15%
		Chainmail Chestplate 15%
		Chainmail Leggings	15%
		Chainmail Boots			15%
		Gold Sword					22%
		Iron Sword					12%
		Diamond Sword				6%
		
		Name Tag						16%
		Saddle							16%
		Obsidian 						16%
		
		Diamond							10%
		Iron Horse Armor		7%
		Gold Horse Armor 		6%
		Diamond Horse Armor 5%

		Enchanted Book			6%				
		Golden Apple				6%
		"""
		
		lootStr = "[]"
		
		return lootStr
	
	#eof _chestContents
	
#eof class

