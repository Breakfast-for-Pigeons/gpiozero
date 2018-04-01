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
		rainbow.yellow.on()
		sleep(sleep_speed)
		rainbow.yellow.off()
		sleep(sleep_speed)
		rainbow.green.on()
		sleep(sleep_speed)
		rainbow.green.off()
		sleep(sleep_speed)
		rainbow.blue.on()
		sleep(sleep_speed)
		rainbow.blue.off()
		sleep(sleep_speed)
		rainbow.purple.on()
		sleep(sleep_speed)
		rainbow.purple.off()
		sleep(sleep_speed)
		rainbow.pink.on()
		sleep(sleep_speed)
		rainbow.pink.off()
		sleep(sleep_speed)
		rainbow.white.on()
		sleep(sleep_speed)
		rainbow.white.off()
		sleep(sleep_speed)
		rainbow.pink.on()
		sleep(sleep_speed)
		rainbow.pink.off()
		sleep(sleep_speed)
		rainbow.purple.on()
		sleep(sleep_speed)
		rainbow.purple.off()
		sleep(sleep_speed)
		rainbow.blue.on()
		sleep(sleep_speed)
		rainbow.blue.off()
		sleep(sleep_speed)
		rainbow.green.on()
		sleep(sleep_speed)
		rainbow.green.off()
		sleep(sleep_speed)
		rainbow.yellow.on()
		sleep(sleep_speed)
		rainbow.yellow.off()
		sleep(sleep_speed)
		rainbow.orange.on()
		sleep(sleep_speed)
		rainbow.orange.off()
	except KeyboardInterrupt:
		print("Stopping program.\n")
		rainbow.close()
		exit()
