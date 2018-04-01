#!/usr/bin/python3
from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(21, 20, 16, 12, 7, 8, 25, 23)
sleep_speed = 1

print("Press Crtl-C to stop the program.")
while True:	
	try:
		leds.on()
		sleep(sleep_speed)
		leds.off()
		sleep(sleep_speed)
		leds.value = (1, 0, 1, 0, 1, 0, 1, 0)
		sleep(sleep_speed)
		leds.blink()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		leds.close()
		exit()
