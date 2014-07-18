# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py

def main():
  mc = minecraft.Minecraft.create(server.address)
  
  mc.postToChat("Hello MCPIPY World!")
  
  mc.setBlocks(0, 0, 0, 100, 0, 0, block.REDSTONE_BLOCK) # червени блокове по Х
  time.sleep(3) # pause 3 seconds
  mc.setBlocks(0, 0, 0, 0, 100, 0, block.EMERALD_BLOCK)  # зелени блокове по Y
  time.sleep(3) # pause 3 seconds
  mc.setBlocks(0, 0, 0, 0, 0, 100, block.LAPIS_BLOCK)    # сини блокове по Z
  time.sleep(3) # pause 3 seconds
  
  
  mc.setBlocks(-10, 0, -10, 10, 0, 10, block.OBSIDIAN)
  time.sleep(3) # pause 3 seconds
  mc.setBlocks(0, -1, -10, 0, 10, 10, block.DIRT)  # пръстена стена по X
  time.sleep(3) # pause 3 seconds
  mc.setBlocks(-10, -1, 0, 10, 10, 0, block.STONE) # каменна стена по Z
  time.sleep(3) # pause 3 seconds
  
  mc.postToChat("Готово :-)")
  print("McPy програмата завърши") 






if __name__ == "__main__":
    main()
