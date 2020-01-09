import time
import board
import neopixel
import bandfkt
 
pixels = bandfkt.initNeopixels(30, neopixel.GRB)

pixels.fill((0,0,0))
pixels.show()
bandfkt.gradient(range(0,30,2), (255, 0, 0), 2)
bandfkt.gradient(range(1,30,2), (255, 255, 0), 2)
time.sleep(0.5)
bandfkt.gradient(range(0,30), (0, 50, 0), 2)
time.sleep(0.5)
bandfkt.gradient(range(1,30,2), (0, 0, 255), 2)
bandfkt.gradient(range(1,30,2), (0, 0, 0), 2)
bandfkt.gradient(range(0,30,2), (0, 200, 150), 2)
time.sleep(0.5)
pixels.fill((255,0,128))
pixels.show()
time.sleep(1)
bandfkt.flackern(range(0,30))
time.sleep(0.5)
bandfkt.flackern(range(0,30))
time.sleep(1)
bandfkt.flackern(range(0,30))
time.sleep(1)
pixels.fill((0,0,0))
pixels.show()
