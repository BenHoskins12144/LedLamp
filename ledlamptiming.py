import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

for n in range(1,3):
  for i in range(20):
    pixels[i] = (0,10,0)
    time.sleep(0.5)
  time.sleep(0.5)
