#from face_detection import face_detection
from MS_API_find_similar import find_similar
from controll_on_off import unlock
from get_distance import get_distance_average,get_distance
from button import button_pressed
import os,time
import RPi.GPIO as GPIO

if __name__ == '__main__':
#	face_detection()
    prev_input = 1
    while(True):
	time.sleep(0.05)
	distance = get_distance()
	print(distance)

	pressed,temp = button_pressed(prev_input)
	print(pressed)
	prev_input = temp
	if(pressed == 1):
	    print("Unlock!")
	    unlock()

	if(distance < 50):
	    os.system("fswebcam -r 640x360 -d /dev/video0 face.jpg")
	    print("pic OK!")
	    confidence = find_similar("face.jpg")
	    if confidence > 0.5:
		print("Unlock!")
		unlock()
	    
