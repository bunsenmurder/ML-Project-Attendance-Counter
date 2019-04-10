import random
import os
import shutil
from PIL import Image

path = r'ImageDB'
nfile=r'Images/RandomFile'
filearray= ['Pos', 'Neg']

i,j=0,0
pos_set = 0

print('How many positive samples do you want?')
p = input()
print('\n')
pos_in = int(p)
print('How many negative samples do you want?')
n = input()
neg_in = int(n)
print('\n')
print('1) Caltech 101 Faces','\n')
print('2) MIT-CBCL Faces','\n')
print('Please select a number representing an option above:')
input = input()
input = int(input)
if input == 1:
    pos_set = 435
    file_ext = '.jpg'
if input == 2:
    pos_set = 3240
    file_ext = '.pgm'
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
        nums = random.sample(range(1,3020), neg_in)
        while j < neg_in:
            text_p = 'neg_' + str(nums[j]) + '.jpg'
            file_path = nfile + '/' + filearray[i] + '/' + text_p
            if text_p in fold_d:
                shutil.copy(fold_p + '/' + text_p, output)
                f.write(str(file_path).rstrip() + '\n')
                j = j + 1
            else:
                print(text_p + ' is not found with fold_d array.')
        f.close()
        nums = []
    if filearray[i] == 'Pos':
        f = open("positives.txt","a+")
        f.truncate(0)
        nums = random.sample(range(1,pos_set + 1), pos_in)
        while j < pos_in:
            text_p = 'pos_' + str(nums[j]) + file_ext
            file_path = nfile + '/' + filearray[i] + '/' + text_p
            if text_p in fold_d:
                shutil.copy(fold_p + '/' + text_p, output)
                f.write(str(file_path).rstrip() + '\n')
                j = j + 1
            else:
                print('Doesnt')
        f.close()
        nums = []
    j = 0
    i = i + 1
