# LEDBoard
These are my experiments based on the documentation here: https://gpiozero.readthedocs.io/en/stable/recipes.html#ledboard
and here: https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#ledboard

![gpiozero_ledboard 3](https://user-images.githubusercontent.com/13591438/38317682-3aca7a52-37f3-11e8-954c-2c7d07b23934.png)

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
Now, just for fun, let's fade the LEDs at different rates:

```python
from gpiozero import LEDBoard
from signal import pause

rainbow = LEDBoard(red=21, orange=20, yellow=16, green=12, blue=7, purple=8, pink=25, white=23, pwm=True)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		rainbow.red.pulse(fade_in_time = 1, fade_out_time = 1, n=None, background=True)
		rainbow.orange.pulse(fade_in_time = 2, fade_out_time = 2, n=None, background=True)
		rainbow.yellow.pulse(fade_in_time = 3, fade_out_time = 3, n=None, background=True)
		rainbow.green.pulse(fade_in_time = 4, fade_out_time = 4, n=None, background=True)
		rainbow.blue.pulse(fade_in_time = 5, fade_out_time = 5, n=None, background=True)
		rainbow.purple.pulse(fade_in_time = 6, fade_out_time = 6, n=None, background=True)
		rainbow.pink.pulse(fade_in_time = 7, fade_out_time = 7, n=None, background=True)
		rainbow.white.pulse(fade_in_time = 8, fade_out_time = 8, n=None, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		rainbow.close()
		exit()
```
