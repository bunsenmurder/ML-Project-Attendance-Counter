#This is the correct formatting file and the only one to be used. It crops the images and resizes them for training.
import os
import random
import shutil

from PIL import Image
import scipy
import scipy.io


print('1) Caltech 101 Faces','\n')
print('2) MIT-CBCL Faces','\n')
print('Please select a number representing an option above:')
input = input()
input = int(input)
print('\n')
if input == 1:
    path = 'ImageDB/101_ObjectCategories/Faces_easy'
    nfile= 'ImageDB/Annotations/Faces_3'
    output = 'ImageDB/Pos_cropped_no_scale'
    output2 = 'ImageDB/Pos'
    for files in os.listdir(output2):
        os.remove(output2 + '/'+ files)
        os.remove(output + '/'+ files)
    for i in range(1,436):
        if i < 10:
            image = 'image_000' + str(i) + '.jpg'
            ant = 'annotation_000' + str(i) + '.mat'
        elif i > 9 and i < 100:
            image = 'image_00' + str(i) + '.jpg'
            ant = 'annotation_00' + str(i) + '.mat'
        elif i > 99 and i < 436:
            image = 'image_0' + str(i) + '.jpg'
            ant = 'annotation_0' + str(i) + '.mat'
        data = scipy.io.loadmat(nfile +'/' + ant)
        coor = data['box_coord'][0]
        x1 = coor[0]
        x2 = coor[1]
        x3 = coor[2]
        x4 = coor[3]
        im = Image.open(path +'/' + image)
        im = im.crop((x3,x1, x4,x2))
        im.save(output + '/' + 'pos_' + str(i) + '.jpg', "JPEG")
        im = im.resize((100, 128), Image.LANCZOS)
        im.save(output2 + '/' + 'pos_' + str(i) + '.jpg', "JPEG", optimize = True, quality=90)
        im.close()

if input == 2:
    path = 'ImageDB/MIT_Pos'
    output = 'ImageDB/Pos'
    for files in os.listdir(output):
        os.remove(output + '/'+ files)
    for filenames in os.listdir(path):
        if filenames.endswith('.pgm'):
            shutil.copy(os.path.join(path,filenames), output)
            

