import tarfile
import shutil
import subprocess
import os

com_cmd = 'cat ImageDB.tar.bz2.aa ImageDB.tar.bz2.ab ImageDB.tar.bz2.ac > ImageDB.tar.bz2'
p = subprocess.Popen(com_cmd, shell=True)
os.waitpid(p.pid, 0)
tf = tarfile.open('ImageDB.tar.bz2', 'r:bz2')
tf.extractall(path = "..")
os.remove('ImageDB.tar.bz2')
print("ImageDB extraction complete!")