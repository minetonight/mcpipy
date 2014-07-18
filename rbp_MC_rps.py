# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py
import random # random generator

def main():
  mc = minecraft.Minecraft.create(server.address)
  
  mc.setBlocks(-1, 0, 0, 1, 0, 3, block.OBSIDIAN) # създава черно поле за игра

  mc.postToChat("<MC RockPaperScissors> Choose your symbols!")
  print("<MC RockPaperScissors> Choose your symbols!")
  time.sleep(0.5)
  
  cpu_choice = random.randint(1, 3)
  player_choice = input("1 = Rock, 2 = Paper, 3 = Scissors. Enter a number:")
  
  message = "It's a draw" #съобщение което ще се запази ако никое условие по-долу не се изпълни
  
  # define winner
  if player_choice == 1:
    if cpu_choice == 3:       # rock vs scissors
      message = "Player wins"
    if cpu_choice == 2:
      message = "CPU wins"    # rock vs paper
      
  if player_choice == 2:
    if cpu_choice == 1:       # paper vs rock
      message = "Player wins"
    if cpu_choice == 3:
      message = "CPU wins"    # paper vs scissors
      
  if player_choice == 3:
    if cpu_choice == 2:       # scissors vs paper
      message = "Player wins"
    if cpu_choice == 1:
      message = "CPU wins"    # scissors vs rock 
      
  
  #define MC blocks
  #   Rock is block.STONE
  #   Paper is block.WOOL
  #   Scissors is block.IRON_BLOCK
  player_block = block.AIR
  cpu_block = block.AIR
  
  if player_choice == 1:
    player_block = block.STONE
  if player_choice == 2:
    player_block = block.WOOL
  if player_choice == 3:
    player_block = block.IRON_BLOCK
  
  if cpu_choice == 1:
    cpu_block = block.STONE
  if cpu_choice == 2:       
    cpu_block = block.WOOL
  if cpu_choice == 3:       
    cpu_block = block.IRON_BLOCK
    
  
  
  
  mc.setBlock(0, 0, 1, player_block)
  mc.setBlock(0, 0, 2, cpu_block) 
  
  mc.postToChat("<MC RockPaperScissors> "+ message) 
  print("<MC RockPaperScissors> " + message) 
  mc.postToChat("<MC RockPaperScissors> Game over.") 
  print("<MC RockPaperScissors> Game over.") 




if __name__ == "__main__":
  main()
