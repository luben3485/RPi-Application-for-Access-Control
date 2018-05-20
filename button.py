import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)
GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)
def button_pressed(prev_input):
	input = GPIO.input(40)
	pressed = 0
#	print("input:" ,input)
	if((not prev_input) and input):
	    print("button pressed")
	    pressed = 1
	prev_input = input
	return pressed,prev_input
