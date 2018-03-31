#!/usr/bin/python3
from gpiozero import LED
from time import sleep

red = LED(21)
sleep_speed = 0.5

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.on()
		sleep(sleep_speed)
		red.off()
		sleep(sleep_speed)
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
