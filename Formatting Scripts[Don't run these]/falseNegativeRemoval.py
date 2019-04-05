# This file is deprecated as the images have alreay be sorted.
# Move this file and FalseNegatives .txt to the root of ImageDB 
import os
path = 'Neg'
f = open('FalseNegatives.txt')
for line in f:
	imgFile = str(path + '/' + line).rstrip()
	if os.path.exists(imgFile):
		os.remove(imgFile)
f.close()
		
