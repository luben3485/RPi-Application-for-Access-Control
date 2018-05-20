import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin = 11
'''
c = input("enter 1 or 0:")
if(int(c) == 1):
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)
if(int(c) == 0):
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)
'''
def unlock():
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.LOW)
    time.sleep(8)
    GPIO.output(11,GPIO.HIGH)




