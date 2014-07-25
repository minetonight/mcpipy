# -*- coding: utf-8 -*-

import mcpi.minecraft as minecraft #import the minecraft.py module from the minecraft directory
import mcpi.block as block #import minecraft block module
import time #import time, so delays can be used
import server # defines where we connect, check server.py
import random

daljina_pole = 20
broy_igrachi = input("Vavedi broya igrachi <7: ")
pozicii = [0] * broy_igrachi

blokove_igrachi = [
  block.FENCE,
  block.NETHER_BRICK_FENCE  ,
  block.COBBLESTONE_WALL,
  block.MOSSY_COBBLESTONE_WALL,
  block.REDSTONE_TORCH_ON,
  block.TORCH,
  ]

tekusht_igrach = 0
student_index = 0

mc = minecraft.Minecraft.create(server.address)
mc.postToChat("МЦ Не се сърди Човече")

#create field
mc.setBlocks(student_index-1, 0, 0,  student_index+1, 2, daljina_pole, block.AIR)
mc.setBlocks(student_index, 0, 0,  student_index, 0, daljina_pole, block.WOOL)
time.sleep(3)

while True:
    zar = random.randint(1, 6)
    mc.postToChat("Играч %s хвърли зар %s" % (tekusht_igrach, zar))
    if pozicii[tekusht_igrach] + zar <= daljina_pole:
        nova_poziciya = pozicii[tekusht_igrach] + zar
        for index_stari_pozicii in range(broy_igrachi):
             if nova_poziciya == pozicii[index_stari_pozicii]:
                 pozicii[index_stari_pozicii] = 0
                 mc.postToChat("Играч %s удари играч %s" % (tekusht_igrach, index_stari_pozicii))
        pozicii[tekusht_igrach] = nova_poziciya
    
    
    sledvasht_igrach = tekusht_igrach + 1
    if sledvasht_igrach == broy_igrachi:
        sledvasht_igrach = 0
           
    for tekushta_poziciya in range(1, daljina_pole + 1):
        block_za_izvejdane = block.AIR
        for index_igrach in range(broy_igrachi):
            if tekushta_poziciya == pozicii[index_igrach]:
                block_za_izvejdane = blokove_igrachi[index_igrach]
        mc.setBlock(student_index, 1, tekushta_poziciya, block_za_izvejdane)

    if pozicii[tekusht_igrach] >= daljina_pole:
        mc.postToChat("Спечели играч: " + str(tekusht_igrach))
        break

    if zar != 6:
      tekusht_igrach = sledvasht_igrach 
    time.sleep(2)


print("McPy програмата завърши") 
