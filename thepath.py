import os
import stat
import shutil


from typing import List

dir_list = os.listdir()
##created a new directory

## Opens the files from the directory
for file in os.walk("/Users/name/project", topdown=True):
    print(file)
    print("------------------")

Movies = ['ET', 'Blade', 'Alien']

## prints current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)
print("-----------------")

directory = ("jo")
parent_dir = "/Users"
## makes a new directory and adds it to /Users directory
path = os.path.join(parent_dir, directory)
print("Directory '%s' created" % directory, "in", parent_dir)
path = "/Users/name/"
print("-----------------")

print("List of directories for file:", path)
print(os.listdir(path))
print("-----------------")
##changes permissions for group in path
os.chmod('/Users/name/afile', stat.S_IRGRP)
print('Permissions changed:\'/Users/name/hotdog.txt\' can be read by group')
path = "/Users/name/project"
print("-----------------")

## if the source throws an error exception
source = "/Users/name/any.txt"
if IsADirectoryError:
    src = source
    print("End of error")
print("-----------------")

## copies a file to a file to a new path from source to new path
metadata = os.stat(source)
destination = "/Users/name/test\n"
dest = shutil.copy2(source, destination)
print("Copying file:")
print(os.listdir(path))
metadata = os.stat(destination)
print("File copy path:", dest)
print("--------END---------")
