# Just for finding best aspect ratio to convert images to.
import os
from PIL import Image
from statistics import mean

width = []
height = []
size = []
ar = []

def round_down(num, divisor):
    num = int(num)
    return num - (num%divisor)
def round_up(num, divisor):
    num = int(num)
    return num + (num%divisor)
cwd = list(os.walk('.'))
cwd = cwd[0][1]
#path = 'training-synthetic'
count = 0
i = 0
print('Inspector starting...','\n')
for folders in cwd:
	print(str(i),') ',cwd[i])
	i+=1 
print('Please select from an option above:')
input = input()
input = int(input)
print('\n')
path = cwd[input]
for filenames in os.listdir(path):
	if filenames.endswith('.jpg'):
            count += 1
            try:
                im = Image.open(os.path.join(path,filenames))
                im.verify()
                im.close()
            except(IOError, SyntaxError) as e:
                print('Bad file: ', filenames)
            width.append(im.width)
            height.append(im.height)
            size.append(im.size)
            aspectratio = width[count-1]/height[count-1]
            ar.append(aspectratio)

'''		
while i < 436:
    image = 'pos_' + str(i) + '.jpg'
    im = Image.open(path +'/' + image)
    width.append(im.width)
    height.append(im.height)
    size.append(im.size)
    aspectratio = width[i-1]/height[i-1]
    ar.append(aspectratio)
    #This is for determining which images are bad to resize if the inital samples product bad results.
    if width[i-1] > height[i-1]:
        print('The image ' + image + ' has a size of ', size[i-1], ' has a width larger than its height.\n')
    i= i +1
'''
avg_ar = mean(ar)
avg_w = mean(width)
avg_h = mean(height)


# Images Information Print
print('Minimum AR is: ' + str(min(ar)) + '\n')
print('Maximum AR is: ' + str(max(ar)) + '\n')
print('Average AR is: ' + str(avg_ar) + '\n')
print('Average Width is: ' + str(avg_w) + '\n')
print('Average Height is: ' + str(avg_h) + '\n')
print('Minimum Width is: ' + str(min(width)) + '\n')
print('Maximum Width is: ' + str(max(width)) + '\n')
print('Minimum Height is: ' + str(min(height)) + '\n')
print('Maximum Height is: ' + str(max(height)) + '\n')
print('Image count is: ' + str(count) + '\n')

# These functions check the aspect ratios of the resolutions
#which are rounded to the nearest multiples of 4 to determine
# Which set of resolutions has the closest to the mean aspect ratio
r1 = abs(avg_ar - round_down(avg_w, 4)/round_down(avg_h, 4))
r2 = abs(avg_ar - round_up(avg_w, 4)/round_up(avg_h, 4))
if r1 < r2:
    print("The best resolution is Width: ", round_down(avg_w, 4)/2, " Height: ", round_down(avg_h, 4)/2)
elif r2 < r1:
    print("The best resolution is Width: ", round_up(avg_w, 4)/2, " Height: ", round_up(avg_h, 4)/2)
else:
    print("The best resolution is the round deafault with  Width: ", int(avg_w)/2, " Height: ", int(avg_h)/2)
