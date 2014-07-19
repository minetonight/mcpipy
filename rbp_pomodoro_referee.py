import os
import time
import random

def playGo():
  """ https://www.ehow.com/how_8348132_play-wav-file-python.html"""
  # Linux
  os.system("aplay -q gogogo.wav")

  # Windows
  # os.system("start /min mplay32 /play /close gogogo.wav")
#eof playGo

time.sleep(10)
while True:
  time.sleep(random.randint(3, 9))
  playGo()
  time.sleep(7) # regroup
  