# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py

def main():
  mc = minecraft.Minecraft.create(server.address) 
  # write the rest of your code here...
  mc.postToChat("Hello MCPIPY World!")
  time.sleep(3) # pause 3 seconds
  #mc.setBlocks(12905 - 200, 60 - 63, -7625-200, -12898 - 200 , 48 - 63, -7631 - 200, block.AIR) # изчистване на блокчето
  mc.setBlocks(12905 - 200, 60 - 63, -7625-200, 12898 - 200 , 52 - 63, -7631 - 200, block.STONE) # изчистване на блокчето

  mc.postToChat("Готово :-)")
  print("McPy програмата завърши")

if __name__ == "__main__":
  main()
