# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py
import random

def main():
  mc = minecraft.Minecraft.create(server.address)
  
  mc.postToChat("Catch me if you can")
  
  borders = 10
  # empty play field
  mc.setBlocks(-1*borders-1, -1*borders-1, -1*borders-1, borders+1, borders+1, borders+1, block.GLOWSTONE_BLOCK)
  mc.setBlocks(-1*borders, -1*borders, -1*borders, borders, borders, borders, block.AIR)
  
  my_name = "Aleks"
  my_block = block.WOOL
  air = block.AIR.id
  my_score = 0
  
  my_x = random.randint(-5, 5)
  my_y = random.randint(-5, 5)
  my_z = random.randint(-5, 5)
  
  
  while True:
    time.sleep(1) # pause 1 second
    command = raw_input("Enter command [W, S, A, D, E, X]:")
    
    new_x = my_x
    new_y = my_y
    new_z = my_z
    
    if (command == "W" or command == "w") and my_x < borders:
      new_x += 1
    if (command == "S" or command == "s") and my_x > -1*borders:
      new_x -= 1
    if (command == "D" or command == "d") and my_z < borders:
      new_z += 1
    if (command == "A" or command == "a") and my_z > -1*borders:
      new_z -= 1
    if (command == "E" or command == "e") and my_y < borders:
      new_y += 1
    if (command == "X" or command == "x") and my_y > -1*borders:
      new_y -= 1
    
    if mc.getBlock(new_x, new_y, new_z) != air:
      my_score += 1
      mc.postToChat("%s got %s pts." % (my_name, my_score))
    
    mc.setBlock(my_x, my_y, my_z, air)
    mc.setBlock(new_x, new_y, new_z, my_block)
  
    my_x = new_x
    my_y = new_y
    my_z = new_z



if __name__ == "__main__":
    main()
