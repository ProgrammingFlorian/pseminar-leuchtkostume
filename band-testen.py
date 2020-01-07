import time
import board
import neopixel
import bandfkt
 
pixels = bandfkt.initNeopixels(7, neopixel.GRB)

pixels.fill((0,0,0))
bandfkt.gradient([0,2,4,6], (0, 0, 0), (255, 0, 0), 2)
bandfkt.gradient([1,3,5], (0, 0, 0), (255, 255, 0), 2)
time.sleep(0.5)
#bandfkt.gradient([1,3,5], (255, 255, 0), (0, 0, 255), 2)
#bandfkt.gradient([1,3,5], (0, 0, 255), (0, 0, 0), 2)
#bandfkt.gradient([0,2,4,6], (255, 0, 0), (0, 200, 150), 2)
#time.sleep(0.5)
pixels.fill((255,0,128))
pixels.show()
time.sleep(1)
bandfkt.flackern(range(0,7))
time.sleep(0.5)
bandfkt.flackern(range(0,7))
time.sleep(1)
bandfkt.flackern(range(0,7))
time.sleep(1)
pixels.fill((0,0,0))
pixels.show()
