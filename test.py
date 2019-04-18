import numpy as np
import sys
import cv2 as cv2
import pandas as pd
import os
from matplotlib import pyplot as plt

#face_cascade = cv2.CascadeClassifier('models/Model5_1/classifier/cascade.xml')
#face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv@3/3.4.5/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

path = 'test/newtest/'
model_path ='models'
output = 'test_results/test_'
#img = cv2.imread(path + im_name)
data = pd.read_csv(path + 'facegroundtruth.txt', sep=" ", header=None)
data.columns = ['file', 'x', 'y', 'w', 'h']
labels = {}
# Create a dictionary object that gathers all the observations for each uniqe key, and stores them under said key.
labels = data.groupby('file')[['x','y','w','h']].apply(lambda g: g.values.tolist()).to_dict()
key_list = list(labels.keys())
#print(type(key_list))
#print(key_list)
results = []
results.append(["file", "Preds", "Hits", "HR", "FA"])
#print(data)
hit_rate = []
false_alarm = []
n = 0
for filename in os.listdir(model_path):
        if filename.endswith('.xml'):
                face_cascade = cv2.CascadeClassifier(os.path.join(model_path,filename))
                for value in key_list:
                        hits = 0
                        img = cv2.imread(path+value)
                        answer_key = np.array(labels[value])
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_cascade.detectMultiScale(
                                gray,
                                #scaleFactor=1.1,
                                minNeighbors=2,
                                minSize=(25, 32),
                                flags=cv2.CASCADE_SCALE_IMAGE)
                        for (fx,fy,fw,fh) in faces:
                                cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)
                                for (x,y,w,h) in answer_key:
                                        if (x in range(fx,fx+fw+1)) and ((x+w) in range(fx,fx+fw+1)):
                                                if (y in range(fy,fy+fh+1)) and ((y+h) in range(fy,fy+fh+1)):
                                                        hits += 1
                                                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        if float(hits/len(answer_key)) > 0:
                                hit_rate.append(float(hits/len(answer_key)))
                                false_alarm.append(float((len(faces) - hits)/len(answer_key)))
                                results.append([value, len(faces), hits, float(hits/len(answer_key)),float((len(faces) - hits)/len(answer_key))])                              
                        cv2.imwrite(output+value,img)
                        #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                #cv2.waitKey(1)

        #print(results)
                print("Hit rate of: ", str(float(sum(hit_rate))/float(len(hit_rate))), "for model", str(filename))
                print("False Positive rate of: ", str(float(sum(false_alarm))/float(len(false_alarm))),"for model", str(filename), "\n")
#final_results = [ map(float, x.split(',') for x in results]
#final_results = np.array(final_results)
#test = np.matrix()
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
        gray,
        #scaleFactor=1.1,
        minNeighbors=2,
        minSize=(25, 32),
        flags=cv2.CASCADE_SCALE_IMAGE
)
print("Detected {0} faces!".format(len(faces)))
#Draw a rectangle around the faces

count = 0
n = 0
for (im,x, y, w, h) in labels:
        if im == im_name:
                n += 1 
                for (fx, fy, fw, fh) in faces:
                        cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)                       
                        if (x in range(fx,fx+fw+1)) and ((x+w) in range(fx,fx+fw+1)):
                            if (y in range(fy,fy+fh+1)) and ((y+h) in range(fy,fy+fh+1)):
                                count += 1
                                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                                cv2.putText(img,str(count), (x,y-5),
                                cv2.FONT_HERSHEY_SIMPLEX,.75,(0,0,255),1, cv2.LINE_AA)

cv2.putText(img,"Predicted Attendance: " + str(len(faces)), (30,60),
cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),1, cv2.LINE_AA)
cv2.putText(img,"Actual Attendance: " + str(count), (30,120),
cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),1, cv2.LINE_AA)
print("The hit count was:", str(count))
print("The True Positive Hit Rate of our classifier was", str(float(count/n)))
print("The False Alarm Rate of our classifier was",str(float((len(faces) - count)/n)))

cv2.imshow("Faces Detected",img)
#cv2.imwrite("class57_test.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
'''
