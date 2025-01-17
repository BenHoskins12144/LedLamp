import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.GP0, 20)

for i in range(0,20):
  pixels[i] = (0,0,100)
  time.sleep(.25)
for i in range(0, 20):
  pixels[-i-1] = (100,0,0)
  time.sleep(0.5)
