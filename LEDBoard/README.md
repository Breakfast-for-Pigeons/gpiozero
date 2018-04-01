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

Here's the next example. This enables pulse width modulation. Each of the LEDs will have a different brightness.

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
