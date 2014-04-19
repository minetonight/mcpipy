#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by burnaron
# http://www.minecraftforum.net/topic/1689199-my-first-script-bunkermaticpy/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import server
import sys, random
from mcpi.vec3 import Vec3



class BunkerBuilder:
  def __init__(self, bunkerCenterTop_vec3, spawn_MC_Ycoord, tunLen, chamberArch, chamberLen, bottomYcoord, material_id, light_id):
    self.x1 = bunkerCenterTop_vec3.x
    self.y1 = bunkerCenterTop_vec3.y
    self.z1 = bunkerCenterTop_vec3.z
    self.long_tun = tunLen
    self.long_arc_ch = chamberArch
    self.long_ch = chamberLen
    self.material_id = material_id
    self.light_id = light_id
    
    self.long_m_ch = long_ch - 2 * self.long_arc_ch
    self.high_c_ch = 3
    self.deepness = self.y1 + spawn_MC_Ycoord - bottomYcoord - self.high_c_ch + 1
  #eof init
  
  
  def build(self):
    
    # Connect to Minecraft.
    try:
      mc = minecraft.Minecraft.create(server.address)
    except:
      print "Cannot connect to Minecraft."
      sys.exit(0)
    
    # FASE 1: cleaning zone
    mc.setBlocks(self.x1-2, self.y1, self.z1-2, self.x1+2, self.y1+20, self.z1+2, 0)
    mc.setBlocks(self.x1-(self.long_tun+self.long_ch+1), self.y1-(self.deepness+1), self.z1-(self.long_tun+self.long_ch+1), self.x1+self.long_tun+self.long_ch+1, self.y1-(self.deepness-self.long_arc_ch-2-1), self.z1+self.long_tun+self.long_ch+1, self.material_id)

    # FASE 2: establishing access
    mc.setBlocks(self.x1-1.5, self.y1+2, self.z1-1.5, self.x1+1.5, self.y1-self.deepness, self.z1+1.5, self.material_id)
    mc.setBlocks(self.x1-1, self.y1+2, self.z1-1, self.x1-1, self.y1-self.deepness, self.z1-1, 0)

    # FASE 3: establishing main tunnels, central chamber & and access stairs
    # FASE 3.1: establishing central chamber
    mc.setBlocks(self.x1-1, self.y1-self.deepness, self.z1-1, self.x1+1, self.y1-(self.deepness-self.high_c_ch), self.z1+1, 0)

    # FASE 3.2: establishing main tunnels
    mc.setBlocks(self.x1-(self.long_tun+self.long_ch), self.y1-self.deepness, self.z1, self.x1+self.long_tun+self.long_ch, self.y1-(self.deepness-1), self.z1, 0)
    mc.setBlocks(self.x1, self.y1-self.deepness, self.z1-(self.long_tun+self.long_ch), self.x1, self.y1-(self.deepness-1), self.z1+self.long_tun+self.long_ch, 0)

    # FASE 3.3: establishing access stairs
    mc.setBlocks(self.x1-1, self.y1+2, self.z1-1, self.x1-1, self.y1-self.deepness, self.z1-1, 65, 3)

    # FASE 4: establishing main chambers
    for pos in range(0, self.long_arc_ch):
        mc.setBlocks(self.x1+self.long_tun+pos, self.y1-self.deepness, self.z1-pos, self.x1+self.long_tun+pos, self.y1-(self.deepness-2)+pos, self.z1+pos, 0)
        mc.setBlocks(self.x1-self.long_tun-pos, self.y1-self.deepness, self.z1-pos, self.x1-self.long_tun-pos, self.y1-(self.deepness-2)+pos, self.z1+pos, 0)
        mc.setBlocks(self.x1-pos, self.y1-self.deepness, self.z1+self.long_tun+pos, self.x1+pos, self.y1-(self.deepness-2)+pos, self.z1+self.long_tun+pos, 0)
        mc.setBlocks(self.x1-pos, self.y1-self.deepness, self.z1-self.long_tun-pos, self.x1+pos, self.y1-(self.deepness-2)+pos, self.z1-self.long_tun-pos, 0)

    mc.setBlocks(self.x1+self.long_tun+self.long_arc_ch, self.y1-self.deepness, self.z1-self.long_arc_ch, self.x1+self.long_tun+self.long_arc_ch+self.long_m_ch, self.y1-(self.deepness-2)+self.long_arc_ch, self.z1+self.long_arc_ch, 0)
    mc.setBlocks(self.x1-(self.long_tun+self.long_arc_ch), self.y1-self.deepness, self.z1-self.long_arc_ch, self.x1-(self.long_tun+self.long_arc_ch)-self.long_m_ch, self.y1-(self.deepness-2)+self.long_arc_ch, self.z1+self.long_arc_ch, 0)
    mc.setBlocks(self.x1-self.long_arc_ch, self.y1-self.deepness, self.z1+self.long_tun+self.long_arc_ch, self.x1+self.long_arc_ch, self.y1-(self.deepness-2)+self.long_arc_ch, self.z1+self.long_tun+self.long_arc_ch+self.long_m_ch, 0)
    mc.setBlocks(self.x1-self.long_arc_ch, self.y1-self.deepness, self.z1-(self.long_tun+self.long_arc_ch), self.x1+self.long_arc_ch, self.y1-(self.deepness-2)+self.long_arc_ch, self.z1-(self.long_tun+self.long_arc_ch)-(self.long_m_ch), 0)

    for pos in range(0, self.long_arc_ch):
        mc.setBlocks(self.x1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.y1-self.deepness, self.z1-self.long_arc_ch+pos, self.x1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.y1-(self.deepness-2)+self.long_arc_ch-pos, self.z1+self.long_arc_ch-pos, 0)
        mc.setBlocks(self.x1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.y1-self.deepness, self.z1-self.long_arc_ch+pos, self.x1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.y1-(self.deepness-2)+self.long_arc_ch-pos, self.z1+self.long_arc_ch-pos, 0)
        mc.setBlocks(self.x1-self.long_arc_ch+pos, self.y1-self.deepness, self.z1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.x1+self.long_arc_ch-pos, self.y1-(self.deepness-2)+self.long_arc_ch-pos, self.z1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, 0)
        mc.setBlocks(self.x1-self.long_arc_ch+pos, self.y1-self.deepness, self.z1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.x1+self.long_arc_ch-pos, self.y1-(self.deepness-2)+self.long_arc_ch-pos, self.z1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, 0)

    # FASE 5: establishing lights & doors:
    # FASE 5.1: central chamber lights:
    mc.setBlock(self.x1, self.y1-(self.deepness-2), self.z1+1, self.light_id * int(random.randint(1, 100)<50))
    mc.setBlock(self.x1+1, self.y1-(self.deepness-2), self.z1, self.light_id * int(random.randint(1, 100)<50))
    mc.setBlock(self.x1, self.y1-(self.deepness-2), self.z1-1, self.light_id * (random.randint(1, 100)<50))
    mc.setBlock(self.x1-1, self.y1-(self.deepness-2), self.z1, self.light_id * (random.randint(1, 100)<50))

    # FASE 5.2: main chambers lights
    #entrance arch
    for pos in range(2, self.long_arc_ch):
        mc.setBlock(self.x1+pos, self.y1-(self.deepness-2), self.z1+self.long_tun+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-pos, self.y1-(self.deepness-2), self.z1+self.long_tun+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+pos, self.y1-(self.deepness-2), self.z1-self.long_tun-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-pos, self.y1-(self.deepness-2), self.z1-self.long_tun-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+pos, self.y1-(self.deepness-2), self.z1+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+pos, self.y1-(self.deepness-2), self.z1-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_tun-pos, self.y1-(self.deepness-2), self.z1+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_tun-pos, self.y1-(self.deepness-2), self.z1-pos, self.light_id * (random.randint(1, 100)<20))

    #walls
    for pos in range(0, self.long_m_ch, 2):
        mc.setBlock(self.x1+self.long_arc_ch, self.y1-(self.deepness-2), self.z1+self.long_tun+self.long_arc_ch+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_arc_ch, self.y1-(self.deepness-2), self.z1+self.long_tun+self.long_arc_ch+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_arc_ch, self.y1-(self.deepness-2), self.z1-(self.long_tun+self.long_arc_ch)-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_arc_ch, self.y1-(self.deepness-2), self.z1-(self.long_tun+self.long_arc_ch)-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+self.long_arc_ch+pos, self.y1-(self.deepness-2), self.z1+self.long_arc_ch, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+self.long_arc_ch+pos, self.y1-(self.deepness-2), self.z1-self.long_arc_ch, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-(self.long_tun+self.long_arc_ch)-pos, self.y1-(self.deepness-2), self.z1+self.long_arc_ch, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-(self.long_tun+self.long_arc_ch)-pos, self.y1-(self.deepness-2), self.z1-self.long_arc_ch, self.light_id * (random.randint(1, 100)<20))

    #inside arch
    for pos in range(0, self.long_arc_ch):
        mc.setBlock(self.x1+self.long_arc_ch-pos, self.y1-(self.deepness-2), self.z1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_arc_ch+pos, self.y1-(self.deepness-2), self.z1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_arc_ch-pos, self.y1-(self.deepness-2), self.z1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-self.long_arc_ch+pos, self.y1-(self.deepness-2), self.z1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.y1-(self.deepness-2), self.z1+self.long_arc_ch-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1+self.long_tun+self.long_arc_ch+self.long_m_ch+pos, self.y1-(self.deepness-2), self.z1-self.long_arc_ch+pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.y1-(self.deepness-2), self.z1+self.long_arc_ch-pos, self.light_id * (random.randint(1, 100)<20))
        mc.setBlock(self.x1-(self.long_tun+self.long_arc_ch)-self.long_m_ch-pos, self.y1-(self.deepness-2), self.z1-self.long_arc_ch+pos, self.light_id * (random.randint(1, 100)<20))
        
    # FASE 5.3: doors
    mc.setBlock(self.x1, self.y1-self.deepness, self.z1+2, 64, self.material_id)
    mc.setBlock(self.x1, self.y1-self.deepness+1, self.z1+2, 64, 8)
    mc.setBlock(self.x1, self.y1-self.deepness+2, self.z1+2, self.material_id)
    mc.setBlock(self.x1, self.y1-self.deepness, self.z1+self.long_tun, 64, 3)
    mc.setBlock(self.x1, self.y1-self.deepness+1, self.z1+self.long_tun, 64, 8)
    mc.setBlock(self.x1, self.y1-self.deepness+2, self.z1+self.long_tun, self.material_id)

    mc.setBlock(self.x1, self.y1-self.deepness, self.z1-2, 64, 3)
    mc.setBlock(self.x1, self.y1-self.deepness+1, self.z1-2, 64, 8)
    mc.setBlock(self.x1, self.y1-self.deepness+2, self.z1-2, self.material_id)
    mc.setBlock(self.x1, self.y1-self.deepness, self.z1-self.long_tun, 64, self.material_id)
    mc.setBlock(self.x1, self.y1-self.deepness+1, self.z1-self.long_tun, 64, 8)
    mc.setBlock(self.x1, self.y1-self.deepness+2, self.z1-self.long_tun, self.material_id)

    mc.setBlock(self.x1+2, self.y1-self.deepness, self.z1, 64, 4)
    mc.setBlock(self.x1+2, self.y1-self.deepness+1, self.z1, 64, 8)
    mc.setBlock(self.x1+2, self.y1-self.deepness+2, self.z1, self.material_id)
    mc.setBlock(self.x1+self.long_tun, self.y1-self.deepness, self.z1, 64, 2)
    mc.setBlock(self.x1+self.long_tun, self.y1-self.deepness+1, self.z1, 64, 8)
    mc.setBlock(self.x1+self.long_tun, self.y1-self.deepness+2, self.z1, self.material_id)
    mc.setBlock(self.x1-2, self.y1-self.deepness, self.z1, 64, 2)
    mc.setBlock(self.x1-2, self.y1-self.deepness+1, self.z1, 64, 8)
    mc.setBlock(self.x1-2, self.y1-self.deepness+2, self.z1, self.material_id)
    mc.setBlock(self.x1-self.long_tun, self.y1-self.deepness, self.z1, 64, 4)
    mc.setBlock(self.x1-self.long_tun, self.y1-self.deepness+1, self.z1, 64, 8)
    mc.setBlock(self.x1-self.long_tun, self.y1-self.deepness+2, self.z1, self.material_id)

    # Phase 6 Chests
    width = self.long_tun+self.long_ch
    depth = self.long_tun+self.long_ch

    mc.setBlock(self.x1+0, self.y1-self.deepness, self.z1+0, 54)

    mc.setBlock(self.x1+0, self.y1-self.deepness, self.z1+width, 54)
    mc.setBlock(self.x1+0, self.y1-self.deepness, self.z1-width, 54)
    mc.setBlock(self.x1+width, self.y1-self.deepness, self.z1+0, 54)
    mc.setBlock(self.x1-width, self.y1-self.deepness, self.z1+0, 54)
  #eof build
  
#eof BunkerBuilder

if __name__ == "__main__":
  #spawn
  x0 = 200
  y0 = 65
  z0 = 200

  # bunker top MC coordinates
  x = 303
  y = 115 
  z = 88
  bottom = 45 # MC y layer coordinate
  material_id = 49
  light_id = 76 # block.REDSTONE_TORCH_ON.id

  x1 = x-x0
  y1 = y-y0
  z1 = z-z0
  long_tun = 4
  long_arc_ch = 7
  long_ch = 30

  vect = Vec3(x1, y1, z1)
  builder = BunkerBuilder(vect, y0, long_tun, long_arc_ch, long_ch, bottom, material_id, light_id)
  builder.build()
#eof main