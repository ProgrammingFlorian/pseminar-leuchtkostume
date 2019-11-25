import RPi.GPIO as GPIO
import time
import rgbfkt

rgbfkt.rgbLedInit()
rgbfkt.gradient((0, 0, 0), (255, 0, 0), 1)
rgbfkt.gradient((255, 0, 0), (255, 0, 255), 5)
rgbfkt.gradient((255, 0, 255), (30, 0, 30), 3)

# Bei Programmende schalten sich alle LEDs aus,
# nicht so wie bei Leuchtband, deshalb Endlos-S
# chleife, damit man das Ergebnis sich beliebig
# lange anschauen kann.
while True:
	pass
