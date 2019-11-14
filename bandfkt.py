import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 7
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def pas(num): # Funktion, um einen Wert zu geben, der sicher für den Leuchtstreifen passt
	if num < 0:
		return 0
	elif num > 255:
		return 255
	else:
		return int(num)

def getSteps(start, end, ltime): # start, end: Tupel mit 3 Werten; ltime: Zeit in Sekunden
	colDiff = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
	step_time = 95 # Bruchteil einer Sekunde, um einen Farb-Schritt zu machen; durch Ausprobieren bestimmt
	return (colDiff[0] / ltime / step_time, colDiff[1] / ltime / step_time, colDiff[2] / ltime / step_time)

def gradient(which_pixels, start, stop, ltime):
	global pixels
	for j in which_pixels:
		pixels[j] = start
	beginTime = time.time()
	steps = getSteps(start, stop, ltime)
##	i = 0
	while time.time() - beginTime <= ltime:
		print(str(i) + " " + str((pixels[0][0], pixels[0][1], pixels[0][2])))
		for j in which_pixels:
			pixels[j] = (pas(pixels[j][0] + steps[0]), pas(pixels[j][1] + steps[1]), pas(pixels[j][2] + steps[2]))
		pixels.show()
##		i += 1
		time.sleep(0.01)
