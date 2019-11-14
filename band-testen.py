import time
import board
import neopixel
import bandfkt
 
pixel_pin = board.D18
num_pixels = 7
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

pixels.fill((0,0,0))
bandfkt.gradient([0,2,4,6], (0, 0, 0), (255, 0, 0), 2)
bandfkt.gradient([1,3,5], (0, 0, 0), (255, 255, 0), 2)
time.sleep(0.5)
bandfkt.gradient([1,3,5], (255, 255, 0), (0, 0, 255), 2)
bandfkt.gradient([1,3,5], (0, 0, 255), (0, 0, 0), 2)
bandfkt.gradient([0,2,4,6], (255, 0, 0), (0, 200, 150), 2)
time.sleep(0.5)
pixels.fill((0,0,0))
