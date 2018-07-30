#!/bin/bash/python
from pathlib import Path
import os, zipfile

print('[INFO] Path objects.')
os.chdir('tmp')
sourcePath = Path(os.getcwd())
print(sourcePath)

print('\n[INFO] ZipFile objects.')
archiveFile = zipfile.ZipFile('tmp.zip')
print(archiveFile.filename)
print(archiveFile.namelist())
print(archiveFile.printdir())

print('\n[INFO] ZipInfo objects.')
print(archiveFile.infolist())
aFile = archiveFile.getinfo('tmp/cats.txt')
print(aFile)
print(aFile.filename)
print('Original size: ' + str(aFile.file_size) + ' bytes.')
print('Compressed size: ' + str(aFile.compress_size) + ' bytes.')
print('Compressed file is %sx smaller!' % (round(aFile.file_size / aFile.compress_size, 2)))
archiveFile.close()