# PIR (Passive Infrared)

These are my experiments based on the documentation here: https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor, here: https://gpiozero.readthedocs.io/en/stable/api_input.html#motion-sensor-d-sun-pir, and here: https://projects.raspberrypi.org/en/projects/physical-computing/13

![pir_led](https://user-images.githubusercontent.com/13591438/38474573-f6e08a36-3b65-11e8-8514-d0ba14bab33f.png)

The example code in the links above turn on an LED when motion is detected. The follow program takes it one step further and creates a timestamped log when motion is detected. If the log doesn't exist, it will create it. If the log already exists, the program will append to it. 

```Python
from gpiozero import LED, MotionSensor
import os, sys, datetime, time

red = LED(pin=21, active_high=True, initial_value=False)
pir = MotionSensor(4)

while True:
    try:
        pir.wait_for_motion()
        logfile = open*("pir_log.txt", "a")
        timestamp = time.asctime(time.localtime(time.time()))
        logfile.write("Motion detected: " + timestamp + "\n")
        logfile.close()
        red.blink(on_time=0.5, off_time=0.5, n=5, background=True)
        pir.wait_for_no_motion()
    except KeyboardInterrupt:
        print("\nStopping program.\n")
        logfile.close()
        pir.close()
        led.close()
        exit()
```

Things I learned about using PIRs with the Raspberry Pi:
* Don't connect to GPIO pin 2 or pin 3. You'll get the following message:
    > gpiozero.exec.PinFixedPull: GPIO2 has a physical pull-up resistor
    > gpiozero.exec.PinFixedPull: GPIO3 has a physical pull-up resistor
