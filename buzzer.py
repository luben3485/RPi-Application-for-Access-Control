import RPi.GPIO as GPIO
import time


buzzer_pin = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin,GPIO.OUT)
pwm_buzzer = GPIO.PWM(buzzer_pin,50)
pwm_buzzer.start(50)

def do():
    pwm_buzzer.ChangeFrequency(261.63)
def re():
    pwm_buzzer.ChangeFrequency(293.66)
def mi():
    pwm_buzzer.ChangeFrequency(329.63)
def fa():
    pwm_buzzer.ChangeFrequency(349.23)
def sol():
    pwm_buzzer.ChangeFrequency(392.00)

def la():
    pwm_buzzer.ChangeFrequency(440.00)
def si():
    pwm_buzzer.ChangeFrequency(493.88)
def udo():
    pwm_buzzer.ChangeFrequency(523.25)
def ure():
    pwm_buzzer.ChangeFrequency(587.33)
def umi():
    pwm_buzzer.ChangeFrequency(659.26)
def ufa():
    pwm_buzzer.ChangeFrequency(698.46)
def usol():
    pwm_buzzer.ChangeFrequency(783.99)
def ula():
    pwm_buzzer.ChangeFrequency(880.00)
def usi():
    pwm_buzzer.ChangeFrequency(987.77)

def doremi():

    
    pwm_buzzer.ChangeFrequency(523)
    time.sleep(1)
    pwm_buzzer.ChangeFrequency(587)
    time.sleep(1)
    pwm_buzzer.ChangeFrequency(659)
    time.sleep(1)
    pwm_buzzer.stop()
    GPIO.cleanup()

def lalala():
	do()
	time.sleep(0.2)
	re()
	time.sleep(0.2)
	mi()
	time.sleep(0.2)
	fa()
	time.sleep(0.2)
	sol()
	time.sleep(0.2)
	la()
	time.sleep(0.2)
	si()
	time.sleep(0.2)
	udo()
	time.sleep(0.2)
	ure()
	time.sleep(0.2)
	umi()
	time.sleep(0.2)
	ufa()
	time.sleep(0.2)
	usol()
	time.sleep(0.2)
	ula()
	time.sleep(0.2)
	usi()
	time.sleep(0.2)
	pwm_buzzer.stop()
	GPIO.cleanup()

def family():
    umi()
    time.sleep(0.4)
    udo()
    time.sleep(0.4)
    usol()
    time.sleep(0.4)
    udo()
    time.sleep(0.4)
    ure()
    time.sleep(0.4)
    usol()
    time.sleep(0.4)
    ure()
    time.sleep(0.4)
    umi()
    time.sleep(0.4)
    ure()
    time.sleep(0.4)
    sol()
    time.sleep(0.4)
    udo()
    pwm_buzzer.stop()
    GPIO.cleanup()

family()	










