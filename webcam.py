import numpy as np
import sys
import cv2 as cv2
from matplotlib import pyplot as plt


face_cascade = cv2.CascadeClassifier('models/model4/classifier/cascade.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        #scaleFactor=1.1,
        minNeighbors=5,
        minSize=(25, 32),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print('Total number of Faces found', len(faces))
 
    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Faces: ' + str(len(faces)), (30,60),
                    cv2.FONT_HERSHEY_SIMPLEX,1.5,(50,205,50),1, cv2.LINE_AA)
    

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("test.jpg", frame)
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
