#!/usr/bin/python3
from gpiozero import PWMLED
from signal import pause

red = PWMLED(21)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.pulse()
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
