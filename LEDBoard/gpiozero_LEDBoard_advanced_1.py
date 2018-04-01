#!/usr/bin/python3
##############################################################################################
# The rainbow is a reminder of God's promise.                                                #
#                                                                                            #
# And God said, "This is the sign of the covenant I am making between me and you and         #
# every living creature with you, a covenant for all generations to come: I have set         #
# my rainbow in the clouds, and it will be the sign of the covenant between me and the       #
# earth. Whenever I bring clouds over the earth and the rainbow appears in the clouds,       #
# I will remember my covenant between me and you and all living creatures of every kind.     #
# Never again will the waters become a flood to destroy all life.                            #
#                                                                                            #
##############################################################################################
from gpiozero import LEDBoard
from signal import pause
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
