# LED

![gpiozero_led](https://user-images.githubusercontent.com/13591438/38166944-4cff442c-34f2-11e8-80c0-6682a3f5df55.png)

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
