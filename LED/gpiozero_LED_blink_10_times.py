#!/usr/bin/python3
from gpiozero import LED
from signal import pause

red = LED(pin=21, active_high=True, initial_value=False)

def release_gpio_pins():
	red.close()
	exit()

def main():
	print("Press Crtl-C to stop the program.")	
	try:
		# Blink 10 times, once every 0.5 seconds, then stop.
		red.blink(on_time=0.5, off_time=0.5, n=10, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		release_gpio_pins()

if __name__ == '__main__':
	main()
