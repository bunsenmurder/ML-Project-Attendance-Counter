import random
import os
import shutil

path = r'ImageDB'
nfile=r'Images/RandomFile'
filearray=os.listdir(path)
i,j=0,0

def randn(i):
    r = random.randint(1,i)
    return(r)


while i < len(filearray):

    fold_p = path + '/' + filearray[i]
    fold_d= os.listdir(fold_p)
    print(fold_p)
    num=len(fold_d) - 1

    # Have it generate random numbers and not use the same one if it has been selected before.
    if filearray[i] == 'Neg':
        print('Neg')
        f = open( nfile+ '/'+ filearray[i] + '/' + "Neg_file_list.txt","a+")
        f.truncate(0)
        while j < 1000:
            ra = randn(num)
            text_p = 'neg_' + str(ra) + '.jpg'

            if text_p in fold_d:
                shutil.copy(fold_p + '/' + text_p, nfile + '/' + filearray[i])
                f.write(text_p + '\n')
                j = j + 1
            else:
                print(text_p + ' is not found with fold_d array.')
        f.close()
    else:
        print('Pos')
        f = open( nfile+ '/'+ filearray[i] + '/' +"Pos_file_list.txt","a+")
        f.truncate(0)
        while j < 100:
            ra= randn(num)
            text_p = 'neg_' + str(ra) + '.jpg'

            if text_p in fold_d:
                shutil.copy(fold_p + '/' + text_p, nfile + '/' + filearray[i])
                f.write(text_p + '\n')
                j = j + 1
            else:
                print('Doesnt')
        f.close()

    j = 0
    i = i + 1
