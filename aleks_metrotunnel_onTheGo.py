#!/usr/bin/env python

#www.stuffaboutcode.com
#Raspberry Pi, Minecraft - auto bridge

# mcpipy.com retrieved from URL below, written by stuffaboutcode
# http://www.stuffaboutcode.com/2013/02/raspberry-pi-minecraft-auto-bridge.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import server


#function to round players float position to integer position
def roundVec3(vec3):
		return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

if __name__ == "__main__":

		time.sleep(2)

		#Connect to minecraft by creating the minecraft object
		# - minecraft needs to be running and in a game
		mc = minecraft.Minecraft.create()

		#Post a message to the minecraft chat window
		mc.postToChat("Hi Minecraft - Metro Tunnel on the Go - Active")

		#Get the players position
		lastPlayerPos = mc.player.getPos()
		counter = 0
		h = 5
		while (True):

				#Get the players position
				playerPos = mc.player.getPos()

				#Find the difference between the player's position and the last position
				movementX = lastPlayerPos.x - playerPos.x
				movementZ = lastPlayerPos.z - playerPos.z

				#Has the player moved more than 0.2 in any horizontal (x,z) direction

				if ((movementX < -0.2) or (movementX > 0.2) or (movementZ < -0.2) or (movementZ > 0.2)):
						mc.postToChat("Your position: x=%s z=%s" % (int(playerPos.x), int(playerPos.z)))

						#Project players direction forward to the next square
						nextPlayerPos = playerPos
						# keep adding the movement to the players location till the next block is found
						while ((int(playerPos.x) == int(nextPlayerPos.x)) and (int(playerPos.z) == int(nextPlayerPos.z))):
								nextPlayerPos = minecraft.Vec3(nextPlayerPos.x - movementX, nextPlayerPos.y, nextPlayerPos.z - movementZ)

						#Is the block below the next player pos air, if so fill it in with 
						blockBelowPos = roundVec3(nextPlayerPos)
						blockBelowPos.z = blockBelowPos.z - 1
						blockBelowPos.y = blockBelowPos.y - 1
						
						aplicate = (movementX < -0.2) or (movementX > 0.2)
						abscissa = (movementZ < -0.2) or (movementZ > 0.2)
						
						mc.postToChat("abscissa = %s" % abscissa)
						mc.postToChat("aplicate = %s" % aplicate)
						
						#floor
						mc.setBlock(blockBelowPos.x, blockBelowPos.y-1, blockBelowPos.z, block.NETHER_RACK)
						mc.setBlock(blockBelowPos.x, blockBelowPos.y, blockBelowPos.z, block.COBBLESTONE_SLAB)
						mc.setBlock(blockBelowPos.x+int(abscissa), blockBelowPos.y-1, blockBelowPos.z+int(aplicate), block.NETHER_RACK)
						mc.setBlock(blockBelowPos.x+int(abscissa), blockBelowPos.y, blockBelowPos.z+int(aplicate), block.COBBLESTONE_SLAB)
						mc.setBlock(blockBelowPos.x-int(abscissa), blockBelowPos.y-1, blockBelowPos.z-int(aplicate), block.NETHER_RACK)
						mc.setBlock(blockBelowPos.x-int(abscissa), blockBelowPos.y, blockBelowPos.z-int(aplicate), block.COBBLESTONE_SLAB)
						
						#air
						mc.setBlocks(blockBelowPos.x+int(abscissa), blockBelowPos.y+1, blockBelowPos.z+int(aplicate), blockBelowPos.x-int(abscissa), blockBelowPos.y+h-1, blockBelowPos.z-int(aplicate), block.AIR)
						
						#walls
						mc.setBlocks(blockBelowPos.x+2*int(abscissa), blockBelowPos.y, blockBelowPos.z+2*int(aplicate), blockBelowPos.x+2*int(abscissa), blockBelowPos.y+h, blockBelowPos.z+2*int(aplicate), block.NETHER_RACK)
						mc.setBlocks(blockBelowPos.x-2*int(abscissa), blockBelowPos.y, blockBelowPos.z-2*int(aplicate), blockBelowPos.x-2*int(abscissa), blockBelowPos.y+h, blockBelowPos.z-2*int(aplicate), block.NETHER_RACK)
						
						#ceiling
						mc.setBlock(blockBelowPos.x+int(abscissa), blockBelowPos.y+h, blockBelowPos.z+int(aplicate), block.NETHER_RACK)
						mc.setBlock(blockBelowPos.x-int(abscissa), blockBelowPos.y+h, blockBelowPos.z-int(aplicate), block.NETHER_RACK)
						if counter % 5 == 0:
							mc.setBlock(blockBelowPos.x, blockBelowPos.y+h, blockBelowPos.z, block.GLOWSTONE_BLOCK)
						else:
							mc.setBlock(blockBelowPos.x, blockBelowPos.y+h, blockBelowPos.z, block.NETHER_RACK)
							


						#Store players last position
						lastPlayerPos = playerPos
						counter += 1

						#Delay
				time.sleep(0.5)