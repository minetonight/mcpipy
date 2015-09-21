# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import server # defines where we connect, check server.py

mc = minecraft.Minecraft.create(server.address)

def fill(start_x, start_y, start_z, length, tall, wide, ID):
    spawn_x = 150
    spawn_y = 69
    spawn_z = 230
    x = start_x - spawn_x
    y = start_y - spawn_y
    z = start_z - spawn_z
    mc.setBlocks(x, y, z, length + x, tall + y, wide + z, ID)

def main():

    # for Mossy brick stone
    start_x = -2447
    start_y = 130
    start_z = -1103

    length = 30
    wide = 30
    tall = 30
    ID = block.Block(98,1)
    fill(start_x, start_y, start_z, length, tall, wide, ID)
    

    # for Brick blocks
    start_x = -2428
    start_y = 130
    start_z = -1160
   
    length = 30
    wide = -30
    tall = 30
    ID = block.BRICK_BLOCK
    fill(start_x, start_y, start_z, length, tall, wide, ID)
    mc.postToChat("END")
if __name__ == "__main__":

    main()
