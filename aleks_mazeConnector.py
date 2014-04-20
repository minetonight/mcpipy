import mcpi.minecraft as minecraft
import mcpi.block as block
import sys, random
from math import *
from random import randint as rand
import server
from mcpi.vec3 import Vec3

class MazeConnector:
	
	def setRange(self, vec3_from, vec3_to):
		self.minX = min(vec3_from.x, vec3_to.x)
		self.minZ = min(vec3_from.z, vec3_to.z)
		self.maxX = max(vec3_from.x, vec3_to.x)
		self.maxZ = max(vec3_from.z, vec3_to.z)
		
		if vec3_from.y != vec3_to.y:
			raise Exception ("provide to corner points on the same level")
		
		self.y_level = vec3_to.y 
	#eof setRange
	
	
	def connect(self, num_junctions):
		
		# Connect to Minecraft.
		try:
			mc = minecraft.Minecraft.create(server.address)
		except:
			print "Cannot connect to Minecraft."
			sys.exit(0)
		
		connections = 0
		
		while connections < num_junctions:
			randX = rand(self.minX, self.maxX)
			randZ = rand(self.minZ, self.maxZ)
			
			if mc.getBlock(randX, self.y_level+1, randZ) == block.AIR.id and mc.getBlock(randX, self.y_level-1, randZ) == block.AIR.id:
				
				#find wall for the ladder
				
				"""    
				0x2: Facing north (for ladders and signs, attached to the north side of a block)
				0x3: Facing south
				0x4: Facing west
				0x5: Facing east"""

				if mc.getBlock(randX, self.y_level-1, randZ+1) != block.AIR.id:
					direction = 0x2 # south it is 2
				elif mc.getBlock(randX-1, self.y_level-1, randZ) != block.AIR.id:
					direction = 0x5 # west not 3
				elif mc.getBlock(randX, self.y_level-1, randZ-1) != block.AIR.id:
					direction = 0x3 # north
				elif mc.getBlock(randX+1, self.y_level-1, randZ) != block.AIR.id:
					direction = 0x4 # east
				else:
					print ("crossroad at %s, %s; skipping" % (randX, randZ))
					continue
				
					
				mc.setBlock(randX, self.y_level, randZ, block.AIR.id)
				mc.setBlock(randX, self.y_level, randZ, block.LADDER.id, direction) 
				mc.setBlock(randX, self.y_level-1, randZ, block.LADDER.id, direction) 
				connections += 1
				print ("conn %s at %s, %s" % (connections, randX, randZ))
		#eof while
		
	#eof connect
	
	
#eof class

