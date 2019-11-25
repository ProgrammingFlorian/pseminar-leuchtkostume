import time
import RPi.GPIO as GPIO

rp = gp = bp = 0
maxPWM = 50

def rgbLedInit():
	global rp, gp, bp
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT, initial=False)
	GPIO.setup(24, GPIO.OUT, initial=False)
	GPIO.setup(23, GPIO.OUT, initial=False)
	rp = GPIO.PWM(25, maxPWM)
	gp = GPIO.PWM(24, maxPWM)
	bp = GPIO.PWM(23, maxPWM)
	rp.start(0)
	gp.start(0)
	bp.start(0)

def rgbToPwm(rgbValue):
	shift = 255.0 / maxPWM
	return (rgbValue[0]/shift, rgbValue[1]/shift, rgbValue[2]/shift)

def pas(num): # Funktion, um einen Wert zu geben, der sicher für den Leuchtstreifen passt
	if num < 0:
		return 0
	elif num > maxPWM:
		return maxPWM
	else:
		return num

def getStep(start, end, ltime): # start, end: Tupel mit 3 Werten; ltime: Zeit in Sekunden
	colDiff = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
	step_time = 95 # Bruchteil einer Sekunde, um einen Farb-Schritt zu machen; durch Ausprobieren bestimmt
	return (colDiff[0] / ltime / step_time, colDiff[1] / ltime / step_time, colDiff[2] / ltime / step_time)

def gradient(start, stop, ltime):
	global rp, gp, bp
	beginTime = time.time()
	start = rgbToPwm(start)
	stop = rgbToPwm(stop)
	step = getStep(start, stop, ltime)
	while time.time() - beginTime <= ltime:
		start = ((start[0]+step[0], start[1]+step[1], start[2]+step[2]))
		rp.ChangeDutyCycle(pas(start[0]))
		gp.ChangeDutyCycle(pas(start[1]))
		bp.ChangeDutyCycle(pas(start[2]))
		time.sleep(0.01)
