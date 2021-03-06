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
