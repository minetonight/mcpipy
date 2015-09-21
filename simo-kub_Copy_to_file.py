# -*- coding: utf-8 -*-

f = open("C:\Python\mcPipy\mcpipy-master\server.txt","w")

#spawn_x = input("Where is the spawn point?(x) :")
#spawn_y = input("Where is the spawn point?(y) :")
#spawn_z = input("Where is the spawn point?(z) :")
#start_point_x = input("Where do you start?(x) :")
#start_point_y = input("Where do you start?(y) :")
#start_point_z = input("Where do you start?(z) :")
#how_long_is_it = input("how long is your line? (x length) : ")
#how_tall_is_it = input("How tall is your line? (y height) : ")
#how_wide_is_it = input("How wide is your line? (z width ) : ")



import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py

def main():
	x = start_point_x - spawn_x
	y = start_point_y - spawn_y
	z = start_point_z - spawn_z
	print(x,y,z)
	mc = minecraft.Minecraft.create(server.address)
	for a in range(how_tall_is_it):
		
		for b in range(how_wide_is_it):
			
			
			for v in range(how_long_is_it):
				current_block = mc.getBlockWithData(x, y, z)
				#blockID=current_block.id
				#blockData=current_block.data
				#current_block = mc.getBlockWithData(x, y, z)
				print("block=" + str(current_block))
				f.write(str(current_block) + "\n")
				#f.write(str(current_block.id) + "," + (current_block.data) + "\n")
				#blk.id +","+ blk.data + '\n'
				
				
				x = x + 1
			x = start_point_x - spawn_x
			z = z + 1	
		mc.postToChat("Level "+ str(a) +" is finished")
		time.sleep(1)
		z = start_point_z - spawn_z
		y = y + 1		
if __name__ == "__main__":
    spawn_x = 200
	spawn_y = 65
	spawn_z = 200
	start_point_x = 
	start_point_y = 
	start_point_z = 
	how_long_is_it = 33
	how_tall_is_it = 33
	how_wide_is_it = 41
	main()

