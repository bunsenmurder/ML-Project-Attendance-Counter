import numpy as np
import sys
import cv2 as cv2
from matplotlib import pyplot as plt

#This is our best model, using the model 3 template with an abv of 4e-5.
#face_cascade2 = cv2.CascadeClassifier('models/Model3_4e-5.xml')
# This is our second best model, using the model 3 template with an abv of 10e-6.
face_cascade = cv2.CascadeClassifier('models/Model3_10e-6.xml')

video_capture = cv2.VideoCapture(0)
#If the above video capture code doesn't work, comment it out and uncomment the one below.
#video_capture =cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #ret2, frame2 = video_capture.read()
    #ret3, frame3 = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        #scaleFactor=2,
        minNeighbors=3,
        minSize=(25, 32),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    '''
    faces2 = face_cascade2.detectMultiScale(
        gray2,
        #scaleFactor=1.3,
        minNeighbors=1,
        minSize=(25, 32),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    #print('Total number of Faces found', len(faces))
    '''
    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Faces: ' + str(len(faces)), (30,60),
                    cv2.FONT_HERSHEY_SIMPLEX,1.5,(50,205,50),1, cv2.LINE_AA)
	
    '''
    for (x, y, w, h) in faces2:
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame2, 'Faces: ' + str(len(faces2)), (30,60),
                    cv2.FONT_HERSHEY_SIMPLEX,1.5,(50,205,50),1, cv2.LINE_AA)
    '''
    # Display the resulting frame
    cv2.imshow('Model3_10e-6', frame)
    #cv2.imshow('Model3_4e-5', frame2)
    #cv2.imshow('Video3', frame3)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        #cv2.imwrite("test.jpg", frame)
        break

# When everything is done, release the capture
video_capture.release()
#video_capture2.release()
cv2.destroyAllWindows()
