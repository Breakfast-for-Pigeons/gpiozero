#!/usr/bin/python3
from gpiozero import LEDBoard
from time import sleep

rainbow = LEDBoard(21, 20, 16, 12, 7, 8, 25, 23)
sleep_speed = 0.05

print("Press Crtl-C to stop the program.")
while True:	
	try:
		rainbow[0].on()			# Turn on the first LED (pin 21).
		sleep(sleep_speed)
		rainbow[4].on()			# Turn on the fifth LED (pin 7).
		sleep(sleep_speed)
		rainbow[0].off()		# Turn off the first LED (pin 21).
		sleep(sleep_speed)
		rainbow[4].off()		# Turn off the fifth LED (pin 7).
		sleep(sleep_speed)
	except KeyboardInterrupt:
		print("Stopping program.\n")
		rainbow.close()
		exit()
