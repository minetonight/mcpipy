#!/usr/bin/env python

#www.stuffaboutcode.com
#Raspberry Pi, Minecraft - hide and seek

# mcpipy.com retrieved from URL below, written by stuffaboutcode
# http://www.stuffaboutcode.com/2013/01/raspberry-pi-minecraft-hide-and-seek.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import math
import server


#function to round players float position to integer position
def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
  
if __name__ == "__main__":

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create(server.address)

    #Post a message to the minecraft chat window
    mc.postToChat("Hi, Minecraft Hide & Seek")

    time.sleep(2)
  
    #Find the players position
    playerPos = mc.player.getPos()
  
    #Create random position within 50 blocks from the player, our hidden block will go there
    randomBlockPos = roundVec3(playerPos)
    randomBlockPos.x = random.randrange(randomBlockPos.x - 50, randomBlockPos.x + 50)
    randomBlockPos.y = random.randrange(randomBlockPos.y - 5, randomBlockPos.y + 5)
    randomBlockPos.z = random.randrange(randomBlockPos.z - 50, randomBlockPos.z + 50)
    print randomBlockPos
  
    #Create hidden diamond block
    mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.DIAMOND_BLOCK)
    mc.postToChat("A diamond has been hidden - go find!")
  
    #Start hide and seek
    seeking = True
    lastPlayerPos = playerPos
    lastDistanceFromBlock = distanceBetweenPoints(randomBlockPos, lastPlayerPos)
    timeStarted = time.time()
    while (seeking == True):
        #Get players position
        playerPos = mc.player.getPos()
        #Has the player moved
        if lastPlayerPos != playerPos:
            distanceFromBlock = distanceBetweenPoints(randomBlockPos, playerPos)
            if distanceFromBlock < 2:
                #found it!
                seeking = False
            else:
                if distanceFromBlock < lastDistanceFromBlock:
                    mc.postToChat("Warmer " + str(int(distanceFromBlock)) + " blocks away")
                if distanceFromBlock > lastDistanceFromBlock:
                    mc.postToChat("Colder " + str(int(distanceFromBlock)) + " blocks away")
          
            lastDistanceFromBlock = distanceFromBlock
          
        time.sleep(2)
    timeTaken = time.time() - timeStarted
    mc.postToChat("Well done - " + str(int(timeTaken)) + " seconds to find the diamond")

    time.sleep(5)
  
    mc.postToChat("www.stuffaboutcode.com")
    
    
"""    TODO
1. multiplayer: 
get all players and iterate them
store them in dictionary with their last coordinates
if player is not in the dictionary, add him with last coordintes

2. not too spammy
iterate every 5-10 seconds
send messages as /w %playername%  if possible

3. eternal program
on each iteration check for connection, and if lost reconnect
sleep 2^tries seconds and try to reconnect

4. file storage
store the current hidden block coordinates in file.
On iteration read the file and if empty generate new treasure
on tresure found erase the file and sleep 6-12h (random)

5. hiding places
read the hidind centres and radii from file (python parse yml?)
the centres are around the overworld portals
hide the block 
 - always in the ground,
 - 1-5 blocks below the surface (read getHeight(x, z))
 - only if the block on the top is in [grass, GRASS_TALL, dirt, stone, gravel, sand, sandstone] 
  (not in player property mostly)
  (not lost in the ocean)
 - precious block random from [block.DIAMOND_BLOCK, LAPIS_LAZULI_BLOCK, GOLD_BLOCK, EMERALD_BLOCK]


"""