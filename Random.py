import random
import os
import shutil

path = r'C:\Users\Kyle\Desktop\Face_DataBase'
nfile=r'C:\Users\Kyle\Desktop\RandomFile'
filearray=os.listdir(path)


nums=[]
i,j=0,0

def randn(k):
    r = random.randint(1,k)
    if r in nums:
        randn(k)
    else:
        nums.append(r)
        return(r)
    
def write_f(file_na,text_p,filea,fold_p):
    f = open( nfile+ '\\'+ filearray[i] + '\\' +file_na,"a+")
    shutil.copy(fold_p + '\\' + text_p, nfile + '\\' + filea)
    f.write(text_p + '\n')
    f.close()
    
while i < len(filearray):
    fold_p = path + '\\' + filearray[i]
    fold_d= os.listdir(fold_p)
    print(fold_p)
    num=len(fold_d) -1
    
    
    if filearray[i] == 'Neg':
        print('Neg')
        file_na = "Neg_file_list.txt"
        while j < 1000:
            ra = randn(num)
            text_p = 'neg_' + str(ra) + '.jpg'
            if text_p in fold_d:
                write_f(file_na,text_p,filearray[i],fold_p)
                j = j + 1
            
    else:
        print('Pos')
        file_na="Pos_file_list.txt"
        while j < 100:
            ra= randn(num)
            text_p = 'pos_' + str(ra) + '.jpg'
            if text_p in fold_d:
                write_f(file_na,text_p,filearray[i],fold_p)
                j = j + 1             
    j = 0
    i = i + 1
    