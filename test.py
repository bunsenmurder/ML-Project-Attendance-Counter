import numpy as np
import sys
import cv2 as cv2
from matplotlib import pyplot as plt


face_cascade = cv2.CascadeClassifier('models/model4/classifier16/cascade.xml')

#video_capture = cv2.VideoCapture(0)

img = cv2.imread('test/Class57.png')
#img = cv2.imread('voyager2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
        gray,
        #scaleFactor=1.1,
        minNeighbors=1,
        minSize=(1, 1),
        flags=cv2.CASCADE_SCALE_IMAGE
)
print("Detected {0} faces!".format(len(faces)))
 
#Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # Display the resulting frame
    #cv2.imshow('Video', frame)

cv2.imshow("Faces Detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
