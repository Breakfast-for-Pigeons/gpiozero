#!/usr/bin/python3
from gpiozero import PWMLED
from signal import pause

red = PWMLED(pin=21, active_high=True, initial_value=0, frequency=100)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.blink(on_time=0.5, off_time=0.5, fade_in_time = 2, fade_out_time = 2, n=None, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
