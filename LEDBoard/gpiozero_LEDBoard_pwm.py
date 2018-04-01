#!/usr/bin/python3
from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(21, 20, 16, 12, 7, 8, 25, 23, pwm=True)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		leds.value = (0.2, 0.3, 0.4, 0.5, 0.6, 1, 0.7, 0.8)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		leds.close()
		exit()
