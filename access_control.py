#from face_detection import face_detection
from MS_API_find_similar import find_similar
from controll_on_off import unlock
from get_distance import get_distance
import os

if __name__ == '__main__':
#	face_detection()
    while(True):
	distance = get_distance()
	print(distance)
	if(distance < 50):
	    os.system("fswebcam -r 640x360 -d /dev/video0 face.jpg")
	    print("pic OK!")
	    confidence = find_similar("face.jpg")
	    if confidence > 0.5:
		print("Unlock!")
		unlock()
	    