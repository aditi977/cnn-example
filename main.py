import numpy as np
import threading
import keyboard
import cv2
import face_recognition

fps = 10 #frame per second
cap = cv2.VideoCapture(0)
continuing = True


def timerExpired():
    global threadTimer
    global continuing
    global frame, face_locations

    if continuing:
        threadTimer = threading.Timer(1/fps, timerExpired)    
        threadTimer.start()
        print("Timer expired")
        face_locations = face_recognition.face_locations(frame)

        
ret, frame = cap.read()
face_locations = [(0,0,0,0)]
threadTimer = threading.Timer(1/fps, timerExpired)    
threadTimer.start()
while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    for(top, right, bottom, left) in face_locations:
        frame = cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),3)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if  cv2.waitKey(1) & keyboard.is_pressed('q'):
        continuing = False
        threadTimer.cancel()
        print("pressed")
        break
    

# When everything done, release the capture

print("EXIT")
cap.release()
cv2.destroyAllWindows()
