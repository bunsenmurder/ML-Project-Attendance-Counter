import os
#Manually formatted images
path = r'../ImageDB'
#Second folder destination for second formatting done in this script.
newfile = r'../ImageDB2'

filearray = ['Neg', 'Pos','falseNeg']

i = 0
y, x, z = 1, 1, 1

while i < len(filearray):
    fold_p = path + '/' + filearray[i]
    fold_d= os.listdir(fold_p)
    j=0
    while j < len(fold_d):
        if ".jpg" in fold_d[j] and filearray[i] == "Neg":
            os.rename(fold_p + '/' + fold_d[j], newfile + '/Neg/neg_' + str(y) + '.jpg')
            y = y + 1
        elif ".jpg" in fold_d[j] and filearray[i] == "falseNeg":
            os.rename(fold_p + '/' + fold_d[j], newfile + '/falseNeg/fpos_'+ str(z) + '.jpg')
            z = z + 1
        j=j+1

    i= i +1
