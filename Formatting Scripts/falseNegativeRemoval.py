import os
path = 'Neg'
f = open('FalseNegatives.txt')
for line in f:
	imgFile = str(path + '/' + line).rstrip()
	if os.path.exists(imgFile):
		os.remove(imgFile)
f.close()
		