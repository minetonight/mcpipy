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
  mc.setBlocks(12895 - 200, 53 - 63, -7615-200, -12888 - 200 , 50 - 63, -7621 - 200, block.AIR) # изчистване на блокчето
  mc.postToChat("Готово :-)")
  print("McPy програмата завърши")

if __name__ == "__main__":
  main()
