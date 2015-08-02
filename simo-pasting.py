# -*- coding: utf-8 -*-

#spawn_x = input("Where is the spawn point?(x) :")
#spawn_y = input("Where is the spawn point?(y) :")
#spawn_z = input("Where is the spawn point?(z) :")
#start_point_x = input("Where do you start?(x) :")
#start_point_y = input("Where do you start?(y) :")
#start_point_z = input("Where do you start?(z) :")
#how_long_is_it = input("how long is your line? (x length) : ")
#how_tall_is_it = input("How tall is your line? (y height) : ")
#how_wide_is_it = input("How wide is your line? (z width ) : ")

import ast
import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py


def main():
	f = open ("simo-Parliament.txt", "r")
	lines = f.readlines()
	line_counter = 0
	
	mc = minecraft.Minecraft.create(server.address)
	mc.postToChat("Parliament 2.0 on steroids with mcPipy")
	x = start_point_x - spawn_x
	y = start_point_y - spawn_y
	z = start_point_z - spawn_z
	for i in range (how_tall_is_it):
		z = start_point_z - spawn_z
		y = y + 1
		for j in range (how_wide_is_it):
				x = start_point_x - spawn_x
				z = z + 1
				for n in range (how_long_is_it):
                                                print(x,y,z)
						#print lines[line_counter]
						mc.setBlock(x, y, z, ast.literal_eval(lines[line_counter]))
						line_counter = line_counter + 1
						x = x + 1
						#time.sleep(0.0625)
						
	
		mc.postToChat("Level "+ str(i) +" is finished")
		time.sleep(1)
	mc.postToChat("Job is finished")
#
if __name__ == "__main__":
	spawn_x = 150
	spawn_y = 69
	spawn_z = 230
	start_point_x = 45-33
	start_point_y = 70
	start_point_z = 232
	how_long_is_it = 33
	how_tall_is_it = 33
	how_wide_is_it = 41
	main()
	
