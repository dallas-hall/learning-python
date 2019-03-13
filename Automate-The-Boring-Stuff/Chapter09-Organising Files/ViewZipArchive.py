#!/bin/bash/python
from pathlib import Path
import os, zipfile

print('[INFO] Path objects.')
os.chdir('zips')
zipPath = Path(os.getcwd())
print(zipPath)

print('\n[INFO] ZipFile objects.')
archiveFile = zipfile.ZipFile('shutil_archive.zip')
print(archiveFile.filename)
print(archiveFile.namelist())
print(archiveFile.printdir())

print('\n[INFO] ZipInfo objects.')
print(archiveFile.infolist())
aFile = archiveFile.getinfo('cats.txt')
print(aFile)
print(aFile.filename)
print('Original size: ' + str(aFile.file_size) + ' bytes.')
print('Compressed size: ' + str(aFile.compress_size) + ' bytes.')
print('Compressed file is %sx smaller!' % (round(aFile.file_size / aFile.compress_size, 2)))
archiveFile.close()
