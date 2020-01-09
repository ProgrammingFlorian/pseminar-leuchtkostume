import time
import board
import neopixel

pixels = 0

class GradientPixel:
	def __init__(self, num, colour, target, ltime):
		self.num = num
		self.colour = colour
		self.step = getSteps(colour, target, ltime)
	def doStep(self):
		self.colour = (self.colour[0] + self.step[0], self.colour[1] + self.step[1], self.colour[2] + self.step[2])
	def getColour(self):
		return (pas(self.colour[0]), pas(self.colour[1]), pas(self.colour[2]))

def initNeopixels(num, order):
	global pixels
	pixel_pin = board.D18
	num_pixels = num
	ORDER = order
	pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
	return pixels

def getSteps(start, end, ltime): # start, end: Tupel mit 3 Werten; ltime: Zeit in Sekunden
	colDiff = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
	step_time = 95 # Bruchteil einer Sekunde, um einen Farb-Schritt zu machen; durch Ausprobieren bestimmt
	return (colDiff[0] / ltime / step_time, colDiff[1] / ltime / step_time, colDiff[2] / ltime / step_time)

def pas(num): # Funktion, um einen Wert zu geben, der sicher für den Leuchtstreifen passt
	if num < 0:
		return 0
	elif num > 255:
		return 255
	else:
		return int(num)


def gradient(which_pixels, stop, ltime):
	global pixels
	gradientPixels = []
	for j in which_pixels:
		gradientPixels.append(GradientPixel(j, pixels[j], stop, ltime))
	beginTime = time.time()
	while time.time() - beginTime <= ltime:
		for pix in gradientPixels:
			pix.doStep()
			pixels[pix.num] = pix.getColour()
		pixels.show()
		time.sleep(0.01)

def flackern(which_pixels):
	global pixels
	start_pixels = []
	for j in which_pixels:
		start_pixels.append(pixels[j])
		pixels[j] = (pas(pixels[j][0] + 128), pas(pixels[j][1] + 128), pas(pixels[j][2] + 128))
	pixels.show()
	time.sleep(0.1)
	for j in which_pixels:
		pixels[j] = start_pixels[j]
	pixels.show()
