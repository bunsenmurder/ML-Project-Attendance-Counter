import numpy as np
import sys
import cv2 as cv2
from matplotlib import pyplot as plt

# For model 5 once it finishes on my home pc, try running the model to each stage based on a range between 1e-5 with the limit being the amount of stages it reaches at 1e-6. Do this by making a copy of the original classifier files. Then using the original make model to 1e-6 as the acceptance ratios. Then go up one stage until it stops misclassifying images in a picture.
face_cascade = cv2.CascadeClassifier('models/model4/classifier16/cascade.xml')

#video_capture = cv2.VideoCapture(0)

img = cv2.imread('test/newtest/Class57.png')
#img = cv2.imread('voyager2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
        gray,
        #scaleFactor=1.1,
        minNeighbors=3,
        minSize=(25, 32),
        flags=cv2.CASCADE_SCALE_IMAGE
)
print("Detected {0} faces!".format(len(faces)))
 
#Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # Display the resulting frame
    #cv2.imshow('Video', frame)

cv2.imshow("Faces Detected",img)
#cv2.imwrite("class57_test.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
