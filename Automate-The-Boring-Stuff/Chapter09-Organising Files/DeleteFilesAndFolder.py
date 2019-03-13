#!/bin/python3

from pathlib import Path
import os, shutil

print('[INFO] Creating directory.')
newFolder = Path('my-folder/')
if not Path.exists(newFolder):
	Path.mkdir(newFolder)
os.chdir(str(newFolder))
sourcePath = Path.cwd()
print(str(sourcePath))
print('Done.')

filenames = ['file1', 'file2', 'file3']
foldernames = ['folder1', 'folder2', 'folder3']

print('[INFO] Creating files.')
for i in range(len(filenames)):
	currentPath = sourcePath / filenames[i]
	print(currentPath)
	currentFile = open(currentPath, 'w')
	currentFile.write(str(currentPath) + '\n')
	currentFile.close()
print('Done.')

print('[INFO] Creating folders.')
for i in range(len(foldernames)):
	currentPath = sourcePath / foldernames[i]
	print(currentPath)
	Path.mkdir(currentPath)

print('[INFO] Deleting folder contents and folder.')
print(str(sourcePath))
# Delete everything inside and the folder itself.
shutil.rmtree(sourcePath)
print('Done.')
