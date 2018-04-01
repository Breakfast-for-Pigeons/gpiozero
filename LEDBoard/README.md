# LEDBoard

![gpiozero_ledboard](https://user-images.githubusercontent.com/13591438/38169094-33b83b98-3526-11e8-940e-045f3ab87f04.png)

Here is an example based on the one given in the gpio documentation. It will first turn on all LEDs. Next, it will turn off all LEDs. Third, it sets the values of the LEDS: 1 is on, 0 is off. So LEDs 1, 3, 5, and 7 will be on, and LEDs 2, 4, 6, and 8 will be off. Fourth, it will blink the LEDs. Since the odd numbered LEDs were set to a value of 1, they will always be on. Only the even numbered LEDs will blink. NOTE: When I say "odd" and "even", I'm not referring to the pin numbers; I'm referring to the order in which they were listed. In the example below, pin assignments 21, 16, 7, and 25 are the odd LEDs and the others are even.

```python
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
```

Here's the next example, which enables pulse width modulation. Each of the LEDs will have a different brightness.

```python
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
```

This next example is from the advanced recipes. It will cycle through the LEDs one by one.

```python
from gpiozero import LEDBoard
from time import sleep

rainbow = LEDBoard(21, 20, 16, 12, 7, 8, 25, 23)
sleep_speed = 1

print("Press Crtl-C to stop the program.")
while True:	
	try:
		for color in rainbow:
			color.on()
			sleep(sleep_speed)
			color.off()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		rainbow.close()
		exit()
```

Setting  up the LEDs using LEDBoard, allows you to access individual LEDs using indexing.

```python
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
```

You can also assign names to the LEDs and reference them that way.

```python
from gpiozero import LEDBoard
from time import sleep

rainbow = LEDBoard(red=21, orange=20, yellow=16, green=12, blue=7, purple=8, pink=25, white=23)
sleep_speed = 0.05

print("Press Crtl-C to stop the program.")
while True:	
	try:
		rainbow.red.on()
		sleep(sleep_speed)
		rainbow.red.off()
		sleep(sleep_speed)
		rainbow.orange.on()
		sleep(sleep_speed)
		rainbow.orange.off()
		sleep(sleep_speed)
	except KeyboardInterrupt:
		print("Stopping program.\n")
		rainbow.close()
		exit()
```
