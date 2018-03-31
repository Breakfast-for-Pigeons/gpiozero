# LED

![gpiozero_led](https://user-images.githubusercontent.com/13591438/38166944-4cff442c-34f2-11e8-80c0-6682a3f5df55.png)

The following code will turn the red LED on and off. How long the LED waits in between is determined by the sleep_speed variable. In this case, the sleep speed is one half second.

```python
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
```

Instead of turning the LED on, waiting, and then turning off, the same thing can be accomplished by using the built-in blink function.

```python
from gpiozero import LED
from signal import pause

red = LED(21)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		# Blink once every 0.5 seconds, indefinitely
		red.blink(on_time=0.5, off_time=0.5, n=None, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
```

Notice that this time there is no sleep_speed variable. This can be accomplished using the blink function's **on_time** and **off_time** parameters. The **n** parameter will determine the number of times the LED will blink. In this case, **n=None** means that the program will run indefinitely (or until someone cancels the program. What if you only wanted the LED to blink 10 times? Just change the **n** parameter to 10.

```python
from gpiozero import LED
from signal import pause

red = LED(21)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		# Blink once every 0.5 seconds, 10 times
		red.blink(on_time=0.5, off_time=0.5, n=10, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
```
 
