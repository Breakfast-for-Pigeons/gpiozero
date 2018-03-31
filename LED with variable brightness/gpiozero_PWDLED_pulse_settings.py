#!/usr/bin/python3
from gpiozero import PWMLED
from signal import pause

red = PWMLED(21)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.pulse(fade_in_time = 2, fade_out_time = 2, n=None, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
