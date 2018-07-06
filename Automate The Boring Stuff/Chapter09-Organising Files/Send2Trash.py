#!/bin/python3

from pathlib import Path
# need to install send2trash with pip
# sudo pip
import send2trash, os


trashPath = Path('/home/dhall/.local/share/Trash/files')
# relative to Path.cwd()
sourcePath = Path('tmp')
filename = 'file-for-trash'

print('[INFO] Creating file and writing to it.')
print(str(sourcePath) + '/' + filename)
file = open('tmp/file-for-trash', 'a')
file.write('This file will go to the recycling bin using send2trash.\n')
file.close()
print('[INFO] Sending file to trash.')
print(str(sourcePath) + '/' + filename)
print('to\n' + str(trashPath))
send2trash.send2trash(str(sourcePath) + '/' + filename)
print('[INFO] Listing files in trash')
for currentFile in os.listdir(str(trashPath)):
	print(currentFile)
