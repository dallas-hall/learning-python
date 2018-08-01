#!/bin/python
import zipfile, os, shutil


def print_info(message):
	print('[INFO] ' + str(message))


print_info('Extracting archive.')
os.chdir('zips')
archive = zipfile.ZipFile('zipfile_archive.zip')
os.makedirs(os.getcwd() + '/extraction/')
os.chdir('extraction/')
print(archive.filename)
print(archive.printdir())
archive.extractall()
archive.close()
print_info('Displaying extracted content.')
for folderName, subfolders, files in os.walk(os.getcwd()):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('There is a subfolder called ' + subfolder)

	for file in files:
		print('There is a file called ' + file)
print_info('Deleting extracted content.')
shutil.rmtree(os.getcwd())


