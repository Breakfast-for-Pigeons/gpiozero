# LED with variable brightness

![gpiozero_led](https://user-images.githubusercontent.com/13591438/38166944-4cff442c-34f2-11e8-80c0-6682a3f5df55.png)

Use pulse width modulation to vary the brightness of an LED. The following prgram uses the built-in blink function with all the parameters set to their defaults.

```python
from gpiozero import PWMLED
from signal import pause

red = PWMLED(pin=21, active_high=True, initial_value=0, frequency=100)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, n=None, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
```

Now try changing the parameters. The code below will cause the the LED to fade in from 0 to full brightness over the course of 2 seconds, fade out from full brightness to zero over the course of 2 second, then turn off for 0.5 seconds befroe fading back in again.

```python
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

```

Now make the LED blink 10 times instead of indefinitely. Just change **n** from *None* to *10*.

```python
from gpiozero import PWMLED
from signal import pause

red = PWMLED(pin=21, active_high=True, initial_value=0, frequency=100)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.blink(on_time=0.5, off_time=0.5, fade_in_time = 2, fade_out_time = 2, n=10, background=True)
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()

```
The  pulse function is almost the same as the blink function except that it doesn't turn the LED on and off. It just fades in and out. Here's a basic pulse program with just the default pulse settings:

```python
from gpiozero import PWMLED
from signal import pause

red = PWMLED(21)

print("Press Crtl-C to stop the program.")
while True:	
	try:
		red.pulse()
		pause()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		red.close()
		exit()
```

Now try adjusting the pulse parameters.

```python
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
```
