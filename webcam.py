import numpy as np
import sys
import cv2 as cv2
from matplotlib import pyplot as plt



face_cascade = cv2.CascadeClassifier(r'C:\opencv342\opencv\build\etc\haarcascades\haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(r'C:\Users\Brandon\Documents\opencv\build\etc\haarcascades\haarcascade_eye.xml')

video_capture = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("test.jpg", frame)
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
