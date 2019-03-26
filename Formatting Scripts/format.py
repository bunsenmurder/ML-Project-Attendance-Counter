import os

path = r'C:\Users\Kyle\Desktop\101_ObjectCategories'
newfile = r'C:\Users\Kyle\Desktop\Face_DataBase'

filearray=os.listdir(path)

i =0
y,x=1,1
sum= 0

while i < len(filearray):
    fold_p = path+ '\' +filearray[i]
    fold_d= os.listdir(fold_p)
    j=0
    while j < len(fold_d):
        if ".jpg" in fold_d[j] and filearray[i] != "Faces_easy":
            os.rename(fold_p + '\' + foldd[j], newfile+'\Neg\neg'+ str(y) +'.jpg')
            y=y+1
        elif ".jpg" in fold_d[j] and filearray[i] == "Faces_easy":
            os.rename(fold_p + '\' + foldd[j], newfile+'\Pos\pos'+ str(x) +'.jpg')
            x=x+1
        j=j+1

    i= i +1
