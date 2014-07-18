# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py

def main():
  mc = minecraft.Minecraft.create(server.address)
  
  mc.postToChat("Enter x, y, z and try to find diamond")
  print("Enter x, y, z and try to find diamond")
  
  x = input("enter x:")
  y = input("enter y:")
  z = input("enter z:")
  
  
  block_id = mc.getBlock(x, y, z) # проверка на блокчето
  
  if block_id == block.DIAMOND_ORE.id:
    print("congratulations, there is a diamond")
    mc.postToChat("congratulations, there is a diamond")
  else:
    print("No, there is just block #" + str(block_id))
    mc.postToChat("No, there is just block #" + str(block_id))
      
      

if __name__ == "__main__":
  main()
