import cv2
import time
import pandas as pd
import numpy as np
from playsound import playsound
# import winsound 



cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

font = cv2.FONT_HERSHEY_PLAIN
S= 'Danger'
a=[]
while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    face=face_cascade.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in face:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    eyes_no=len(face)
    if face == ():
        a.append(time.process_time ())
        if a[len(a)-1] - a[0]>1:
            #cv2.putText(frame, str(S), (10,150), font, 3, (0,0,255), 3)
            cv2.putText(frame, str('status :'), (10,180), font, 3, (0,0,255), 3)
            cv2.putText(frame, str('sleep'), (210,180), font, 3, (0,0,255), 3)
            # winsound.PlaySound("mixkit-classic-alarm-995.wav", winsound.SND_FILENAME)
            playsound("tic-tac-27828.mp3")
            print('you are sleeping')  
    else:
        a=[]
    cv2.putText(frame, str('status :'), (10,180), font, 3, (0,0,255), 3)
    cv2.putText(frame, str('Stay at home'), (10,50), font, 2, (0,255,0), 2)
    cv2.putText(frame, str('time : '), (10,80), font, 2, (200,0,200), 2)
    cv2.putText(frame, str(time.ctime()), (110,80), font, 2, (200,0,200), 2) 
    cv2.putText(frame, str(eyes_no), (170,110), font, 2, (200,0,200), 2)  
    cv2.putText(frame, str('eyes no : '), (10,110), font, 2, (200,0,200), 2)
    cv2.imshow('video',frame)
    key=cv2.waitKey(1)
    if key ==ord('v'): 
        break
cap.release()
cv2.destroyAllWindows()

