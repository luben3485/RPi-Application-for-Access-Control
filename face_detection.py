import cv2
import numpy
from MS_API_find_similar import find_similar
from controll_on_off import unlock
def face_detection():
    face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_default.xml') 
    eye_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_eye.xml') 
    cap = cv2.VideoCapture(0) 

    while(True): 
        ret, img = cap.read() 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        for (x,y,w,h) in faces:
	    if x != 0:
		cv2.imwrite("face.jpg",img)
 		confidence = find_similar("face.jpg")
		print(confidence)
		if confidence > 0.5:
		    unlock()
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w] 
#            eyes = eye_cascade.detectMultiScale(roi_gray) 
#            for (ex,ey,ew,eh) in eyes: 
#                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
        cv2.imshow('img',img) 
        if cv2.waitKey(30) & 0xFF == ord('q'): 
            break 
    cap.release() 
    out.release() 
    cv2.destroyAllWindows()
