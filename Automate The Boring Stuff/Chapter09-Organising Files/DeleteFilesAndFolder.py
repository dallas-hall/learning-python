#!/bin/python3

from pathlib import Path
import os

print('[INFO] Creating directory.')
newFolder = Path('my-folder/')
if not Path.exists(newFolder):
	Path.mkdir(newFolder)
os.chdir(str(newFolder))
sourcePath = Path.cwd()
print(str(sourcePath))
print('Done.')

filenames = ['file1', 'file2', 'file3']

print('[INFO] Creating files.')
for i in range(len(filenames)):
	currentPath = sourcePath / filenames[i]
	print(currentPath)
	currentFile = open(currentPath, 'w')
	currentFile.write(str(currentPath) + '\n')
	currentFile.close()
print('Done.')

print('[INFO] Deleting files.')
for currentFile in os.listdir(str(sourcePath)):
	print(sourcePath / currentFile)
	Path.unlink(sourcePath / currentFile)
print('Done.')

print('[INFO] Deleting directory.')
print(str(sourcePath))
# Must be empty
Path.rmdir(sourcePath)
print('Done.')
