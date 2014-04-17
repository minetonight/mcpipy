#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by burnaron
# http://www.minecraftforum.net/topic/1689199-my-first-script-bunkermaticpy/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import random
import server



#parameters
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
#eof parameters


# do not edit below
x1 = x-x0
y1 = y-y0 
z1 = z-z0
mc = minecraft.Minecraft.create(server.address)
long_tun = 4
long_arc_ch = 7
long_ch = 30
long_m_ch = long_ch - 2 * long_arc_ch
high_c_ch = 3
deepness = y1 + y0 - bottom-high_c_ch+1

# FASE 1: cleaning zone
mc.setBlocks(x1-2,y1,z1-2,x1+2,y1+20,z1+2,0)
mc.setBlocks(x1-(long_tun+long_ch+1),y1-(deepness+1),z1-(long_tun+long_ch+1),x1+long_tun+long_ch+1,y1-(deepness-long_arc_ch-2-1),z1+long_tun+long_ch+1, material_id)

# FASE 2: establishing access
mc.setBlocks(x1-1.5,y1+2,z1-1.5,x1+1.5,y1-deepness,z1+1.5, material_id)
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-deepness,z1-1,0)

# FASE 3: establishing main tunnels, central chamber & and access stairs
# FASE 3.1: establishing central chamber
mc.setBlocks(x1-1,y1-deepness,z1-1,x1+1,y1-(deepness-high_c_ch),z1+1,0)

# FASE 3.2: establishing main tunnels
mc.setBlocks(x1-(long_tun+long_ch),y1-deepness,z1,x1+long_tun+long_ch,y1-(deepness-1),z1,0)
mc.setBlocks(x1,y1-deepness,z1-(long_tun+long_ch),x1,y1-(deepness-1),z1+long_tun+long_ch,0)

# FASE 3.3: establishing access stairs
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-deepness,z1-1,65,3)

# FASE 4: establishing main chambers
for pos in range(0,long_arc_ch):
    mc.setBlocks(x1+long_tun+pos,y1-deepness,z1-pos,x1+long_tun+pos,y1-(deepness-2)+pos,z1+pos,0)
    mc.setBlocks(x1-long_tun-pos,y1-deepness,z1-pos,x1-long_tun-pos,y1-(deepness-2)+pos,z1+pos,0)
    mc.setBlocks(x1-pos,y1-deepness,z1+long_tun+pos,x1+pos,y1-(deepness-2)+pos,z1+long_tun+pos,0)
    mc.setBlocks(x1-pos,y1-deepness,z1-long_tun-pos,x1+pos,y1-(deepness-2)+pos,z1-long_tun-pos,0)

mc.setBlocks(x1+long_tun+long_arc_ch,y1-deepness,z1-long_arc_ch,x1+long_tun+long_arc_ch+long_m_ch,y1-(deepness-2)+long_arc_ch,z1+long_arc_ch,0)
mc.setBlocks(x1-(long_tun+long_arc_ch),y1-deepness,z1-long_arc_ch,x1-(long_tun+long_arc_ch)-long_m_ch,y1-(deepness-2)+long_arc_ch,z1+long_arc_ch,0)
mc.setBlocks(x1-long_arc_ch,y1-deepness,z1+long_tun+long_arc_ch,x1+long_arc_ch,y1-(deepness-2)+long_arc_ch,z1+long_tun+long_arc_ch+long_m_ch,0)
mc.setBlocks(x1-long_arc_ch,y1-deepness,z1-(long_tun+long_arc_ch),x1+long_arc_ch,y1-(deepness-2)+long_arc_ch,z1-(long_tun+long_arc_ch)-(long_m_ch),0)

for pos in range(0,long_arc_ch):
    mc.setBlocks(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-deepness,z1-long_arc_ch+pos,x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_arc_ch-pos,0)
    mc.setBlocks(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-deepness,z1-long_arc_ch+pos,x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_arc_ch-pos,0)
    mc.setBlocks(x1-long_arc_ch+pos,y1-deepness,z1+long_tun+long_arc_ch+long_m_ch+pos,x1+long_arc_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_tun+long_arc_ch+long_m_ch+pos,0)
    mc.setBlocks(x1-long_arc_ch+pos,y1-deepness,z1-(long_tun+long_arc_ch)-long_m_ch-pos,x1+long_arc_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1-(long_tun+long_arc_ch)-long_m_ch-pos,0)

# FASE 5: establishing lights & doors:
# FASE 5.1: central chamber lights:
mc.setBlock(x1,y1-(deepness-2),z1+1, light_id * int(random.randint(1, 100)<50))
mc.setBlock(x1+1,y1-(deepness-2),z1, light_id * int(random.randint(1, 100)<50))
mc.setBlock(x1,y1-(deepness-2),z1-1, light_id * (random.randint(1, 100)<50))
mc.setBlock(x1-1,y1-(deepness-2),z1, light_id * (random.randint(1, 100)<50))

# FASE 5.2: main chambers lights
#entrance arch
for pos in range(2,long_arc_ch):
    mc.setBlock(x1+pos,y1-(deepness-2),z1+long_tun+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-pos,y1-(deepness-2),z1+long_tun+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+pos,y1-(deepness-2),z1-long_tun-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-pos,y1-(deepness-2),z1-long_tun-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+pos,y1-(deepness-2),z1+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+pos,y1-(deepness-2),z1-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_tun-pos,y1-(deepness-2),z1+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_tun-pos,y1-(deepness-2),z1-pos, light_id * (random.randint(1, 100)<20))

#walls
for pos in range(0,long_m_ch,2):
    mc.setBlock(x1+long_arc_ch,y1-(deepness-2),z1+long_tun+long_arc_ch+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_arc_ch,y1-(deepness-2),z1+long_tun+long_arc_ch+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_arc_ch,y1-(deepness-2),z1-(long_tun+long_arc_ch)-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_arc_ch,y1-(deepness-2),z1-(long_tun+long_arc_ch)-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+long_arc_ch+pos,y1-(deepness-2),z1+long_arc_ch, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+long_arc_ch+pos,y1-(deepness-2),z1-long_arc_ch, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-(long_tun+long_arc_ch)-pos,y1-(deepness-2),z1+long_arc_ch, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-(long_tun+long_arc_ch)-pos,y1-(deepness-2),z1-long_arc_ch, light_id * (random.randint(1, 100)<20))

#inside arch
for pos in range(0, long_arc_ch):
    mc.setBlock(x1+long_arc_ch-pos,y1-(deepness-2),z1+long_tun+long_arc_ch+long_m_ch+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_arc_ch+pos,y1-(deepness-2),z1+long_tun+long_arc_ch+long_m_ch+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_arc_ch-pos,y1-(deepness-2),z1-(long_tun+long_arc_ch)-long_m_ch-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-long_arc_ch+pos,y1-(deepness-2),z1-(long_tun+long_arc_ch)-long_m_ch-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2),z1+long_arc_ch-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2),z1-long_arc_ch+pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2),z1+long_arc_ch-pos, light_id * (random.randint(1, 100)<20))
    mc.setBlock(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2),z1-long_arc_ch+pos, light_id * (random.randint(1, 100)<20))
    
# FASE 5.3: doors
mc.setBlock(x1,y1-deepness,z1+2,64, material_id)
mc.setBlock(x1,y1-deepness+1,z1+2,64,8)
mc.setBlock(x1,y1-deepness+2,z1+2, material_id)
mc.setBlock(x1,y1-deepness,z1+long_tun,64,3)
mc.setBlock(x1,y1-deepness+1,z1+long_tun,64,8)
mc.setBlock(x1,y1-deepness+2,z1+long_tun, material_id)

mc.setBlock(x1,y1-deepness,z1-2,64,3)
mc.setBlock(x1,y1-deepness+1,z1-2,64,8)
mc.setBlock(x1,y1-deepness+2,z1-2, material_id)
mc.setBlock(x1,y1-deepness,z1-long_tun,64, material_id)
mc.setBlock(x1,y1-deepness+1,z1-long_tun,64,8)
mc.setBlock(x1,y1-deepness+2,z1-long_tun, material_id)

mc.setBlock(x1+2,y1-deepness,z1,64,4)
mc.setBlock(x1+2,y1-deepness+1,z1,64,8)
mc.setBlock(x1+2,y1-deepness+2,z1, material_id)
mc.setBlock(x1+long_tun,y1-deepness,z1,64,2)
mc.setBlock(x1+long_tun,y1-deepness+1,z1,64,8)
mc.setBlock(x1+long_tun,y1-deepness+2,z1, material_id)
mc.setBlock(x1-2,y1-deepness,z1,64,2)
mc.setBlock(x1-2,y1-deepness+1,z1,64,8)
mc.setBlock(x1-2,y1-deepness+2,z1, material_id)
mc.setBlock(x1-long_tun,y1-deepness,z1,64,4)
mc.setBlock(x1-long_tun,y1-deepness+1,z1,64,8)
mc.setBlock(x1-long_tun,y1-deepness+2,z1, material_id)

# Phase 6 Chests
width = long_tun+long_ch
depth = long_tun+long_ch

mc.setBlock(x1+0, y1-deepness, z1+0, 54)

mc.setBlock(x1+0, y1-deepness, z1+width, 54)
mc.setBlock(x1+0, y1-deepness, z1-width, 54)
mc.setBlock(x1+width, y1-deepness, z1+0, 54)
mc.setBlock(x1-width, y1-deepness, z1+0, 54)

