import tarfile
import shutil
import subprocess
import os

com_cmd = 'cat ImageDB.tar.bz2.aa ImageDB.tar.bz2.ab ImageDB.tar.bz2.ac > ImageDB.tar.bz2'
subprocess.check_output(['bash', '-c', com_cmd])
tf = tarfile.open('ImageDB.tar.bz2', 'r:bz2')
tf.extractall(path = "..")
tf.close()
os.remove('ImageDB.tar.bz2')
print("ImageDB extraction complete!")
