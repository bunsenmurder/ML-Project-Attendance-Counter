import random
import os
import shutil
from PIL import Image

path = r'ImageDB'
nfile=r'Images/RandomFile'
filearray= ['Pos', 'Neg']

i,j=0,0

print('How many positive samples do you want?')
p = input()
print('\n')
pos_in = int(p)
print('How many negative samples do you want?')
n = input()
neg_in = int(n)

while i < len(filearray):
    fold_p = path + '/' + filearray[i]
    fold_d= os.listdir(fold_p)
    output = nfile + '/' + filearray[i]
    for files in os.listdir(output):
        os.remove(output + '/'+ files)

    # Have it generate random numbers and not use the same one if it has been selected before.
    if filearray[i] == 'Neg':
        f = open("negatives.txt","a+")
        f.truncate(0)
        nums = random.sample(range(1,7897), neg_in)
        while j < neg_in:
            imNeg = 'neg_' + str(nums[j]) + '.jpg'
            file_path = output + '/' + imNeg
            try:#Error checking to ensure no Image is corrupt.
                if imNeg in fold_d:
                    im = Image.open(os.path.join(fold_p,imNeg))
                    im.verify()
                    im.close()
                    shutil.copy(fold_p + '/' + imNeg, output)
                    f.write(str(file_path).rstrip() + '\n')
                    j = j + 1
            except(IOError, SyntaxError) as e:
                    print('Bad file, please remove: ',imNeg)
                    break
        f.close()
        nums = []
    if filearray[i] == 'Pos':
        f = open("positives.txt","a+")
        f.truncate(0)
        nums = random.sample(range(1,435), pos_in)
        while j < pos_in:
            imPos = 'pos_' + str(nums[j]) + '.jpg'
            file_path = output + '/' + imPos
            try:
                if imPos in fold_d:
                    im = Image.open(os.path.join(fold_p,imPos))
                    im.verify()
                    im.close()
                    shutil.copy(fold_p + '/' + imPos, output)
                    f.write(str(file_path).rstrip() + '\n')
                    j = j + 1
            except(IOError, SyntaxError) as e:
                print('Bad file, please remove: ',imPos)
                break
        f.close()
        nums = []
    j = 0
    i = i + 1
