# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py
mc = minecraft.Minecraft.create(server.address)

def put_grass(start_x,start_z,end_x,end_z):
	current_block_id = 0
	for x in range(start_x, end_x):
		for z in range(start_z, end_z):
			current_block_id = mc.getBlock(x,-1,z)
			if not (current_block_id == block.WATER.id or current_block_id == block.WATER_FLOWING.id or current_block_id == block.WATER_STATIONARY.id):
				mc.setBlock(x, -1, z, block.GRASS)

def main():
	mc.setBlocks(-2485-200, 0, -1243-200, -2236-200 , 200, -1031-200, block.AIR)
	mc.setBlocks(-2485-200, 0, -1031-200, -2285-200 , 200, -981-200, block.AIR)
	mc.setBlocks(-2485-200, 0, -981-200, -2313-200 , 200, -947-200, block.AIR)
	put_grass(-2485-200, -1243-200, -2236-200, -1031-200)
	put_grass(-2485-200, -1031-200, -2285-200 , -981-200)
	put_grass(-2485-200, -981-200, -2313-200, -947-200)

	mc.postToChat("Готово clean Martincho :-)")	
	print "Clean Martincho finish" 


if __name__ == "__main__":
    main()
